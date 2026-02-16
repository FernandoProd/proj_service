from django.db import models
from machines.models import Machine
from orders.models import OrderDetail
from django.utils import timezone

class Schedule(models.Model):
    STATUS_CHOICES = [
        ('waiting', 'Ожидание'),
        ('in_progress', 'В работе'),
        ('done', 'Готово'),
    ]

    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    order_detail = models.ForeignKey(OrderDetail, on_delete=models.CASCADE)
    start_time = models.DateTimeField('Плановое начало')
    end_time = models.DateTimeField('Плановое окончание')
    actual_start_time = models.DateTimeField('Фактическое начало', null=True, blank=True)
    actual_end_time = models.DateTimeField('Фактическое окончание', null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='waiting')

    def __str__(self):
        return f"Станок {self.machine.m_name} - {self.order_detail.detail.name} с {self.start_time} по {self.end_time}"