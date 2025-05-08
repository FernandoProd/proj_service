from django.urls import path
from .views import schedule_view, run_auto_schedule, mark_schedule_complete

urlpatterns = [
    path('', schedule_view, name='schedule'),
    path('run-auto-schedule/', run_auto_schedule, name='run_auto_schedule'),
    path('mark-schedule-complete/<int:schedule_id>/', mark_schedule_complete, name='mark_schedule_complete'),  # Новый путь для изменения статуса
]