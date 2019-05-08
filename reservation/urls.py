from django.urls import path
from . import views

urlpatterns = [
    path('', views.reservations, name='reservations'),
    path('reserve/', views.reserve, name='reserve')
]
