from django.db import models
from machines.models import Machine
from orders.models import OrderDetail

class Schedule(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, verbose_name='Станок')
    order_detail = models.ForeignKey(OrderDetail, on_delete=models.CASCADE, verbose_name='Деталь в заявке')
    start_time = models.DateTimeField('Начало')
    end_time = models.DateTimeField('Окончание')
    is_complete = models.BooleanField('Завершено', default=False)

    def __str__(self):
        return f"{self.machine.m_name} — {self.order_detail.detail.name} ({self.start_time.date()})"

    class Meta:
        verbose_name = 'План'
        verbose_name_plural = 'Планы'
        ordering = ['start_time']
