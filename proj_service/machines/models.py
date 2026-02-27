from django.db import models

class Machine(models.Model):
    m_name = models.CharField('Название станка', max_length=40)
    machine_type = models.CharField('Тип станка', max_length=100)
    status = models.CharField(max_length=20, choices=[('свободен', 'Свободен'), ('занят', 'Занят')])
    full_text = models.TextField('Описание')
    working_hours_per_day = models.FloatField('Часы работы в день', default=8.0)

    def __str__(self):
        return self.m_name

    def get_absolute_url(self):
        return f'/machines/{self.id}'

    class Meta:
        verbose_name = 'Станок'
        verbose_name_plural = 'Станки'


#m_name machine_type status full_text