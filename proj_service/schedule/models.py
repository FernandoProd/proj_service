from django.db import models
from machines.models import Machine
from orders.models import OrderDetail
from django.utils import timezone

class Schedule(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    order_detail = models.ForeignKey(OrderDetail, on_delete=models.CASCADE)
    start_time = models.DateTimeField('Время начала')
    end_time = models.DateTimeField('Время окончания')

    def __str__(self):
        return f"Станок {self.machine.m_name} - {self.order_detail.detail.name} с {self.start_time} по {self.end_time}"

    class Meta:
        verbose_name = 'План работы'
        verbose_name_plural = 'Планы работы'