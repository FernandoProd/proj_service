from django.contrib import admin
from .models import Schedule
from .utils import schedule_production  # Импортируем функцию, которая обновляет расписание

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('machine', 'order_detail', 'start_time', 'end_time')  # Поля, которые будут отображаться в списке
    search_fields = (
        'machine__m_name', 'order_detail__order__order_number', 'order_detail__detail__name')  # Поиск по этим полям
    list_filter = ('machine', 'order_detail__order__deadline')  # Фильтрация по этим полям
    ordering = ('start_time',)  # Сортировка по времени начала

    # Добавляем действие для обновления расписания
    actions = ['update_schedule']

    def update_schedule(self, request, queryset):
        # Вызываем функцию, которая обновляет расписание
        schedule_production()  # или schedule_production(queryset) если нужно работать с queryset

        # Уведомление о том, что расписание обновлено
        self.message_user(request, "Расписание обновлено!")

    update_schedule.short_description = 'Обновить расписание'