from django.utils import timezone
from datetime import timedelta
from collections import defaultdict
from orders.models import OrderDetail
from machines.models import Machine
from .models import Schedule


def schedule_production():
    Schedule.objects.all().delete()

    #Делаем фильтраци по деталям, отсеиваем все, кроме тех, которые в ожидании или процессе
    order_details = OrderDetail.objects.select_related('order', 'detail') \
        .filter(status__in=['pending', 'in_process']) \
        .order_by('order__deadline')

    for machine in Machine.objects.all():          #Создание индивидуального расписания под каждый станок
        current_time = timezone.now()

        #Отбор подходящих деталей под конкретный станок
        compatible_orders = [od for od in order_details if machine in od.detail.machines.all()]

        #Группировка по detail.id, чтобы их делать подряд и не учитывать время на подготовку повторно
        grouped = defaultdict(list)  #Список OrderDetail, который будет содержать все одинаковые детали из всех заказов
        for od in compatible_orders:
            grouped[od.detail.id].append(od)
        #Само построение расписания
        for detail_id, group in grouped.items():
            detail = group[0].detail
            is_first = True  #Флаг для того, чтобы все идентичные детали в полседующем не тратили prep_time

            for od in group:
                for i in range(od.quantity):  #Так как в заявке может быть несколько одинаковых деталей, проходим каждую как отдельную единицу
                    start_time = current_time
                    duration = detail.piece_time
                    if is_first:
                        duration += detail.prep_time
                        is_first = False
                    end_time = start_time + timedelta(minutes=duration)

                    Schedule.objects.create(
                        machine=machine,
                        order_detail=od,
                        start_time=start_time,
                        end_time=end_time
                    )
                    current_time = end_time
