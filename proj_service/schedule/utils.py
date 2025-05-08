from datetime import timedelta
from django.utils import timezone
from orders.models import OrderDetail
from machines.models import Machine
from .models import Schedule

def auto_schedule():
    start_time = timezone.now()
    work_day = timedelta(hours=8)

    # Получаем все незапланированные детали
    order_details = OrderDetail.objects.filter(status='pending')

    for od in order_details:
        detail = od.detail
        quantity = od.quantity

        # Подходящие станки
        machines = detail.machines.all()

        if not machines.exists():
            continue  # Нет подходящих станков — пропускаем

        total_minutes = detail.prep_time + detail.piece_time * quantity
        duration = timedelta(minutes=total_minutes)

        # Пытаемся поставить детали друг за другом, если они одинаковые
        for machine in machines:
            latest_schedule = Schedule.objects.filter(machine=machine).order_by('-end_time').first()

            # Если станок занят, пробуем поставить после окончания предыдущей работы
            if latest_schedule:
                available_start = max(start_time, latest_schedule.end_time)
            else:
                available_start = start_time

            end_time = available_start + duration

            # Не планируем за пределами смены
            if (end_time - available_start) > work_day:
                continue

            # Если станок свободен, планируем деталь
            if machine.status == 'свободен':  # Проверяем, свободен ли станок
                # Создаём запись в расписании
                Schedule.objects.create(
                    machine=machine,
                    order_detail=od,
                    start_time=available_start,
                    end_time=end_time,
                )

                # Обновляем статус детали на "в работе"
                od.status = 'in_process'
                od.save()

                # Обновляем статус станка на "занят"
                machine.status = 'занят'
                machine.save()

                break  # Назначено — не продолжаем к другим станкам



def mark_schedule_as_complete(schedule_id):
    # Получаем расписание
    schedule = Schedule.objects.get(id=schedule_id)
    machine = schedule.machine
    order_detail = schedule.order_detail

    # Обновляем статус детали на "в процессе"
    order_detail.status = 'in_process'
    order_detail.save()

    # Обновляем статус станка на "занят"
    machine.status = 'занят'
    machine.save()

    # Обновляем статус расписания как завершённый
    schedule.is_complete = True
    schedule.save()