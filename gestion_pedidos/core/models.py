from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils import timezone

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    descripcion = RichTextField(null=True, blank=True)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    
    fecha_creacion = models.DateTimeField(default=timezone.now) 
    
    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    creado = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, default='Pendiente')

    def __str__(self):
        return f'Pedido #{self.id}'


class PedidoProducto(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def subtotal(self):
        return self.cantidad * self.producto.precio

class Perfil(models.Model):
    # Relación 1 a 1: Cada usuario tiene UN solo perfil
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    
    avatar = models.ImageField(upload_to='avatares/', null=True, blank=True)
    biografia = models.TextField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    
    def __str__(self):
        return f"Perfil de {self.user.username}"