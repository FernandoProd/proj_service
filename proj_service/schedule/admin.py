from django.contrib import admin
from .models import Schedule
from .utils import schedule_production

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('machine', 'order_detail', 'start_time', 'end_time')
    search_fields = (
        'machine__m_name', 'order_detail__order__order_number', 'order_detail__detail__name')
    list_filter = ('machine', 'order_detail__order__deadline')
    ordering = ('start_time',)

    actions = ['update_schedule']

    def update_schedule(self, request, queryset):
        schedule_production()
        self.message_user(request, "Расписание обновлено!")

    update_schedule.short_description = 'Обновить расписание'