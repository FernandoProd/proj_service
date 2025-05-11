from django.utils import timezone
from datetime import timedelta
from collections import defaultdict
from orders.models import OrderDetail
from machines.models import Machine
from .models import Schedule


def schedule_production():
    Schedule.objects.all().delete()

    # Исключаем завершённые детали
    order_details = OrderDetail.objects.select_related('order', 'detail') \
        .filter(status__in=['pending', 'in_process']) \
        .order_by('order__deadline')

    for machine in Machine.objects.all():
        current_time = timezone.now()

        # Отбираем подходящие детали
        compatible_orders = [od for od in order_details if machine in od.detail.machines.all()]

        # Группируем по detail.id
        grouped = defaultdict(list)
        for od in compatible_orders:
            grouped[od.detail.id].append(od)

        for detail_id, group in grouped.items():
            detail = group[0].detail
            is_first = True  # Чтобы один раз применить prep_time

            for od in group:
                for i in range(od.quantity):
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
