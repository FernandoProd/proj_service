# schedule/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Пример простого URL-обработчика
    path('', views.schedule_home, name='schedule_home'),
]