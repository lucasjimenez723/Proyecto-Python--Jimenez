from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('nuevo-pedido/', views.nuevo_pedido, name='nuevo_pedido'),
    path('pedido/<int:pedido_id>/agregar-producto/', views.agregar_producto, name='agregar_producto'),
]
