from django.contrib import admin
from .models import Pedido, Producto, DetallePedido

admin.site.register(Pedido)
admin.site.register(Producto)
admin.site.register(DetallePedido)
