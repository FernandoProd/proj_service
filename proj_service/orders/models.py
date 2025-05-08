from django.db import models
from machines.models import Machine
from django.utils import timezone
from datetime import timedelta

class Detail(models.Model):
    name = models.CharField('Наименование', max_length=100)
    number = models.CharField('Номер детали', max_length=50, unique=True)
    material = models.CharField('Материал', max_length=100)
    prep_time = models.IntegerField('Время подготовительное (мин)')   #validators=[MaxValueValidator(10 000)]  По идее могут быть ошибки от int и ошибки, если число будет больше 10^4
    piece_time = models.IntegerField('Время штучное (мин)')
    length = models.FloatField('Длина (мм)', )    #Тут было б ы правильно обсуждать размеры заготовки, а не самой детали, тк все эти данные из АСУПр в теории идут в производство
    width = models.FloatField('Ширина (мм)', )
    height = models.FloatField('Высота (мм)', )
    machines = models.ManyToManyField(Machine, verbose_name='Подходящие станки')

    def __str__(self):
        return f"{self.number} - {self.name}"

    class Meta:    #Этот класс существуюет для переименования модели в админке
        verbose_name = 'Деталь'
        verbose_name_plural = 'Детали'


class Order(models.Model):
    customer = models.CharField('Клиент', max_length=100)
    order_number = models.CharField('Номер заявки', max_length=100, unique=True)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    priority = models.IntegerField('Приоритет', default=1)                     #чем меньше число, тем выше его приоритет
    customer_name = models.CharField('Наименование прибора', max_length=100)
    deadline = models.DateField('Дедлайн', default=timezone.now() + timedelta(days=7))
    status = models.CharField('Статус', max_length=100)

    def __str__(self):
        return f"Заявка №{self.id} от {self.customer} (до {self.deadline})"

    class Meta:    #Этот класс существуюет для переименования модели в админке
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


class OrderDetail(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Ожидает'),
        ('in_process', 'В работе'),
        ('done', 'Завершено'),
    ]

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_details')
    detail = models.ForeignKey(Detail, on_delete=models.CASCADE, related_name='order_details')
    quantity = models.PositiveIntegerField('Количество')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.detail.name} x{self.quantity} для заявки #{self.order.id}"

    class Meta:
        unique_together = ('order', 'detail')
