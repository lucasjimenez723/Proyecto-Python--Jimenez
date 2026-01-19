from django.contrib import admin
from .models import Producto, Pedido, PedidoProducto

admin.site.register(Producto)
admin.site.register(Pedido)
admin.site.register(PedidoProducto)
