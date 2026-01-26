from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('crear/', views.crear_pedido, name='crear_pedido'),
    path('pedido/<int:pedido_id>/', views.detalle_pedido, name='detalle_pedido'),
    path('item/<int:item_id>/eliminar/', views.eliminar_item, name='eliminar_item'),
    path('registro/', views.registro, name='registro'),
    path('perfil/', views.mi_perfil, name='mi_perfil'),
    path('menu/', views.ProductoListView.as_view(), name='productos_list'),
    path('menu/nuevo/', views.ProductoCreateView.as_view(), name='producto_create'),
    path('menu/<int:pk>/editar/', views.ProductoUpdateView.as_view(), name='producto_update'),
    path('menu/<int:pk>/borrar/', views.ProductoDeleteView.as_view(), name='producto_delete'),
    path('about/', views.about, name='about'),
]
