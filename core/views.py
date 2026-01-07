from django.shortcuts import render, redirect, get_object_or_404
from .models import Pedido, Producto, DetallePedido


def home(request):
    pedidos = Pedido.objects.all()
    return render(request, 'core/home.html', {'pedidos': pedidos})


def nuevo_pedido(request):
    if request.method == 'POST':
        cliente = request.POST.get('cliente')
        pedido = Pedido.objects.create(cliente=cliente)
        return redirect('agregar_producto', pedido_id=pedido.id)

    return render(request, 'core/nuevo_pedido.html')


def ver_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    return render(request, 'core/ver_pedido.html', {
        'pedido': pedido
    })
def pedido_detalle(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    return render(request, 'core/pedido_detalle.html', {
        'pedido': pedido
    })

def agregar_producto(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    productos = Producto.objects.all()

    if request.method == 'POST':
        producto_id = request.POST.get('producto')
        cantidad = int(request.POST.get('cantidad'))

        producto = get_object_or_404(Producto, id=producto_id)
        DetallePedido.objects.create(
            pedido=pedido,
            producto=producto,
            cantidad=cantidad
        )
        return redirect('agregar_producto', pedido_id=pedido.id)

    detalles = DetallePedido.objects.filter(pedido=pedido)

    return render(request, 'core/agregar_producto.html', {
        'pedido': pedido,
        'productos': productos,
        'detalles': detalles
    })