from django.shortcuts import render, redirect, get_object_or_404
from .models import Pedido, Producto, DetallePedido
from .forms import PedidoForm
from django.contrib import messages  


def nuevo_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pedido creado correctamente')
            return redirect('dashboard')
    else:
        form = PedidoForm()

    return render(request, 'core/nuevo_pedido.html', {'form': form})

def tablero(request):
    pedidos = Pedido.objects.all().order_by('-fecha')
    total_pedidos = pedidos.count()
    total_ventas = sum(p.total for p in pedidos)

    context = {
        'pedidos': pedidos,
        'total_pedidos': total_pedidos,
        'total_ventas': total_ventas,
    }

    return render(request, 'core/dashboard.html', context)


def agregar_producto(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)

    if request.method == 'POST':
        producto_id = request.POST.get('producto')
        cantidad = int(request.POST.get('cantidad', 1))

        producto = get_object_or_404(Producto, id=producto_id)

        detalle, creado = DetallePedido.objects.get_or_create(
            pedido=pedido,
            producto=producto,
            defaults={'cantidad': cantidad}
        )

        if not creado:
            detalle.cantidad += cantidad
            detalle.save()

        return redirect('dashboard')

    productos = Producto.objects.all()
    return render(request, 'core/agregar_producto.html', {
        'pedido': pedido,
        'productos': productos
    })

def detalle_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    detalles = pedido.detalles.all()  # related_name='detalles'

    context = {
        'pedido': pedido,
        'detalles': detalles,
        'total': pedido.total,
    }

    return render(request, 'core/detalle_pedido.html', context)

def sumar_producto(request, detalle_id):
    detalle = get_object_or_404(DetallePedido, id=detalle_id)
    detalle.cantidad += 1
    detalle.save()
    return redirect('detalle_pedido', pedido_id=detalle.pedido.id)

def restar_producto(request, detalle_id):
    detalle = get_object_or_404(DetallePedido, id=detalle_id)
    detalle.cantidad -= 1

    if detalle.cantidad <= 0:
        detalle.delete()
    else:
        detalle.save()

    return redirect('detalle_pedido', pedido_id=detalle.pedido.id)

def eliminar_producto(request, detalle_id):
    detalle = get_object_or_404(DetallePedido, id=detalle_id)
    pedido_id = detalle.pedido.id
    detalle.delete()
    return redirect('detalle_pedido', pedido_id=pedido_id)


