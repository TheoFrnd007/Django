from django.urls import path
from . import views

urlpatterns = [
    path('usuarios/', views.usuarios, name='usuarios'),
    path('registro/', views.registro, name='registro'),
]