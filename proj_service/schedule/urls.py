from django.urls import path
from . import views

urlpatterns = [
    path('', views.schedule_home, name='schedule_home'),
    path('refresh/', views.refresh_schedules, name='refresh_schedules'),
    path('mark/<int:pk>/<str:status>/', views.mark_schedule_status, name='mark_schedule_status'),
]