from django.urls import path
from . import views

urlpatterns = [
    path('', views.tablero, name='dashboard'),
    path('nuevo-pedido/', views.nuevo_pedido, name='nuevo_pedido'),
    path('pedido/<int:pedido_id>/agregar-producto/', views.agregar_producto, name='agregar_producto'),
    path('pedido/<int:pedido_id>/', views.detalle_pedido, name='detalle_pedido'),
    path(
    'detalle/<int:detalle_id>/sumar/',
    views.sumar_producto,
    name='sumar_producto'
),
path(
    'detalle/<int:detalle_id>/restar/',
    views.restar_producto,
    name='restar_producto'
),
path(
    'detalle/<int:detalle_id>/eliminar/',
    views.eliminar_producto,
    name='eliminar_producto'
),

]

