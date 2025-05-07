from django.db import models

class Detail(models.Model):
    name = models.CharField('Номер детали', max_length=100, unique=True)
    number = models.CharField('Наименование', max_length=50, unique=True)
    material = models.CharField('Материал', max_length=100)
    prep_time = models.IntegerField('Время подготовительное (мин)')   #validators=[MaxValueValidator(10 000)]  По идее могут быть ошибки от int и ошибки, если число будет больше 10^4
    piece_time = models.IntegerField('Время штучное (мин)')
    length = models.FloatField('Длина (мм)', )    #Тут было б ы правильно обсуждать размеры заготовки, а не самой детали, тк все эти данные из АСУПр в теории идут в производство
    width = models.FloatField('Ширина (мм)', )
    height = models.FloatField('Высота (мм)', )

    def __str__(self):
        return f"{self.number} - {self.name}"

    class Meta:    #Этот класс существуюет для переименования модели в админке
        verbose_name = 'Деталь'
        verbose_name_plural = 'Детали'


class Order(models.Model):
    order_number = models.CharField('Номер заявки', max_length=100, unique=True)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    priority = models.IntegerField('Приоритет', default=1)                     #чем меньше число, тем выше его приоритет
    customer_name = models.CharField('Имя кастомное', max_length=100)
    status = models.CharField('Статус', max_length=100)

    def __str__(self):
        return f"Заявка {self.order_number}"

    class Meta:    #Этот класс существуюет для переименования модели в админке
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_details')
    detail = models.ForeignKey(Detail, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.detail.number} x{self.quantity} ({self.order.order_number})"

    class Meta:
        unique_together = ('order', 'detail')
