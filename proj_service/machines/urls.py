from django.urls import path
from . import views

urlpatterns = [
    path('', views.machines_home, name='machines_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.MachineDetailView.as_view(), name='machine-detail'),
    path('<int:pk>/update', views.MachineUpdateView.as_view(), name='machine-update'),
    path('<int:pk>/delete', views.MachineDeleteView.as_view(), name='machine-delete'),
]