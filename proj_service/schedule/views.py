from django.shortcuts import render, redirect
from .models import Schedule
from .utils import auto_schedule, mark_schedule_as_complete
from django.views.decorators.http import require_POST
from django.contrib import messages

def schedule_view(request):
    plans = Schedule.objects.select_related('machine', 'order_detail__detail').order_by('start_time')
    return render(request, 'schedule/schedule_view.html', {'plans': plans})

@require_POST
def run_auto_schedule(request):
    auto_schedule()
    messages.success(request, "Автоматическое планирование выполнено.")
    return redirect('schedule')  # имя URL'а для страницы с расписанием

@require_POST
def mark_schedule_complete(request, schedule_id):
    try:
        # Обновляем статус расписания и статус станка
        mark_schedule_as_complete(schedule_id)
        messages.success(request, "Деталь теперь в процессе, станок занят.")
    except Schedule.DoesNotExist:
        messages.error(request, "Не удалось найти расписание.")
    return redirect('schedule')  # редирект обратно на страницу с расписанием