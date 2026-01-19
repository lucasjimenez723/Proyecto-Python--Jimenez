from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('pedido/crear/', views.crear_pedido, name='crear_pedido'),
    path('pedido/<int:pedido_id>/', views.detalle_pedido, name='detalle_pedido'),

    path('item/eliminar/<int:item_id>/', views.eliminar_item, name='eliminar_item'),

    path('registro/', views.registro, name='registro'),
]
