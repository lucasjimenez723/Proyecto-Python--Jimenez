from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nombre


class Pedido(models.Model):
    ESTADOS = (
        ('pendiente', 'Pendiente'),
        ('preparacion', 'En preparación'),
        ('entregado', 'Entregado'),
    )

    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')

    def total(self):
        return sum(item.subtotal() for item in self.items.all())

    def __str__(self):
        return f"Pedido #{self.id}"


class PedidoProducto(models.Model):
    pedido = models.ForeignKey(
        Pedido,
        related_name='items',
        on_delete=models.CASCADE
    )
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def subtotal(self):
        return self.producto.precio * self.cantidad

    def __str__(self):
        return f"{self.producto.nombre} x{self.cantidad}"
