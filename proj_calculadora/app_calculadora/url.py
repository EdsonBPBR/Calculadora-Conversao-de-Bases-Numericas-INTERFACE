from django.urls import path
from .views import inicio
from django.shortcuts import redirect

app_name = 'app_calculadora'

urlpatterns = [
    path('app_calculadora/inicio/', inicio, name='inicio')
]
