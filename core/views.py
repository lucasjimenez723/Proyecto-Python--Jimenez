from django.shortcuts import render, get_object_or_404, redirect
from .models import Pedido, Producto, PedidoProducto

def index(request):
    pedidos = Pedido.objects.all()
    return render(request, 'core/index.html', {'pedidos': pedidos})


def detalle_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    items = pedido.items.select_related('producto')
    productos = Producto.objects.all()

    if request.method == 'POST':
        producto_id = request.POST.get('producto')
        cantidad = int(request.POST.get('cantidad', 1))

        producto = get_object_or_404(Producto, id=producto_id)

        item, creado = PedidoProducto.objects.get_or_create(
            pedido=pedido,
            producto=producto
        )

        if not creado:
            item.cantidad += cantidad
        else:
            item.cantidad = cantidad

        item.save()
        return redirect('detalle_pedido', pedido_id=pedido.id)

    return render(request, 'core/detalle_pedido.html', {
        'pedido': pedido,
        'items': items,
        'productos': productos
    })


def eliminar_item(request, item_id):
    item = get_object_or_404(PedidoProducto, id=item_id)
    pedido_id = item.pedido.id
    item.delete()
    return redirect('detalle_pedido', pedido_id=pedido_id)


def cambiar_estado(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    estados = ['pendiente', 'preparacion', 'entregado']
    actual = estados.index(pedido.estado)
    pedido.estado = estados[(actual + 1) % len(estados)]
    pedido.save()
    return redirect('detalle_pedido', pedido_id=pedido.id)
