from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Pedido, Producto, PedidoProducto


@login_required
def index(request):
    pedidos = Pedido.objects.filter(cliente=request.user)
    return render(request, 'core/index.html', {'pedidos': pedidos})


@login_required
def crear_pedido(request):
    pedido = Pedido.objects.create(cliente=request.user)
    return redirect('detalle_pedido', pedido.id)


@login_required
def detalle_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id, cliente=request.user)
    items = PedidoProducto.objects.filter(pedido=pedido)
    productos = Producto.objects.all()

    if request.method == 'POST':
        producto_id = request.POST['producto']
        cantidad = int(request.POST['cantidad'])

        producto = get_object_or_404(Producto, id=producto_id)

        PedidoProducto.objects.create(
            pedido=pedido,
            producto=producto,
            cantidad=cantidad
        )

        return redirect('detalle_pedido', pedido.id)

    total = sum(item.subtotal() for item in items)

    return render(request, 'core/detalle_pedido.html', {
        'pedido': pedido,
        'items': items,
        'productos': productos,
        'total': total
    })


@login_required
def eliminar_item(request, item_id):
    item = get_object_or_404(PedidoProducto, id=item_id)
    pedido_id = item.pedido.id
    item.delete()
    return redirect('detalle_pedido', pedido_id)


def registro(request):
    if request.method == 'POST':
        User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password']
        )
        return redirect('login')

    return render(request, 'core/registro.html')
