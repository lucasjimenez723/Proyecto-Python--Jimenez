from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pedido/<int:pedido_id>/', views.detalle_pedido, name='detalle_pedido'),
    path('item/eliminar/<int:item_id>/', views.eliminar_item, name='eliminar_item'),
    path('pedido/<int:pedido_id>/estado/', views.cambiar_estado, name='cambiar_estado'),
]
