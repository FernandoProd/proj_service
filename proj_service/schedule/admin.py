from django.contrib import admin
from .models import Schedule
from orders.models import OrderDetail
from machines.models import Machine

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('machine', 'order_detail', 'start_time', 'end_time', 'is_complete')
    list_filter = ('machine', 'is_complete')
    autocomplete_fields = ('order_detail', 'machine')

    # Обязательно: включаем поля, по которым будет поиск в выпадающих списках
    search_fields = (
        'order_detail__detail__name',         # имя детали
        'order_detail__order__order_number',  # номер заявки
        'machine__name',                      # имя станка
    )

