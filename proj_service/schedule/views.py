from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from .models import Schedule
from .utils import schedule_production
from collections import defaultdict
from django.utils.timezone import localdate


from django.utils.timezone import localdate

def schedule_home(request):
    schedules = Schedule.objects.select_related('machine', 'order_detail', 'order_detail__order', 'order_detail__detail') \
        .order_by('start_time')

    #Привязка к дате и станкам
    grouped_schedule = defaultdict(lambda: defaultdict(list))
    for s in schedules:
        day = localdate(s.start_time)
        grouped_schedule[day.strftime('%d.%m.%Y')][s.machine.m_name].append(s)  # Форматируем дату

    #Преобразование defaultdict в обычный словарь, так как ничего не отображалось на странице
    grouped_schedule = {
        str(day): {machine_name: list(schedules) for machine_name, schedules in machines.items()}
        for day, machines in grouped_schedule.items()
    }

    return render(request, 'schedule/schedule_view.html', {'grouped_schedule': grouped_schedule})


@csrf_protect             #Защита, чтобы не выполнялись лишние действия
def refresh_schedules(request):           #Кнопка обновления плана
    if request.method == 'POST':
        schedule_production()
        messages.success(request, 'Планы успешно обновлены.')
    return redirect('schedule_home')


@csrf_protect
def mark_schedule_status(request, pk, status):          #Изменение статуса
    from django.shortcuts import get_object_or_404
    from django.utils import timezone

    schedule = get_object_or_404(Schedule, pk=pk)
    schedule.status = status

    if status == 'in_progress':
        schedule.actual_start_time = timezone.now()
    elif status == 'done':
        schedule.actual_end_time = timezone.now()

    schedule.save()
    return redirect('schedule_home')