from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('crear/', views.crear_pedido, name='crear_pedido'),
    path('pedido/<int:pedido_id>/', views.detalle_pedido, name='detalle_pedido'),
    path('item/<int:item_id>/eliminar/', views.eliminar_item, name='eliminar_item'),
    path('registro/', views.registro, name='registro'),
    path('perfil/', views.mi_perfil, name='mi_perfil'),
]
