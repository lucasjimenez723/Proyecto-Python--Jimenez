from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Pedido, Producto, PedidoProducto
from django.contrib.auth.decorators import login_required
from .forms import UserEditForm, PerfilForm 
from .models import Perfil
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

@login_required
def home(request):
    pedidos = Pedido.objects.filter(cliente=request.user)
    return render(request, 'core/home.html', {'pedidos': pedidos})


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

@login_required
def mi_perfil(request):
    # Aseguramos que el usuario tenga un perfil creado (por si es un usuario viejo)
    perfil, created = Perfil.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        # Cargamos los datos enviados en ambos formularios
        user_form = UserEditForm(request.POST, instance=request.user)
        perfil_form = PerfilForm(request.POST, request.FILES, instance=perfil)

        if user_form.is_valid() and perfil_form.is_valid():
            user_form.save()
            perfil_form.save()
            # Redirigimos a la misma página para ver los cambios
            return redirect('mi_perfil')
    else:
        # Si es GET, mostramos los formularios con los datos actuales
        user_form = UserEditForm(instance=request.user)
        perfil_form = PerfilForm(instance=perfil)

    context = {
        'user_form': user_form,
        'perfil_form': perfil_form,
        'perfil': perfil, # Pasamos el perfil para mostrar el avatar actual
    }
    return render(request, 'core/perfil.html', context)


class ProductoListView(ListView):
    model = Producto
    template_name = 'core/productos_list.html'
    context_object_name = 'productos'


class ProductoCreateView(LoginRequiredMixin, CreateView):
    model = Producto
    template_name = 'core/producto_form.html'
    fields = ['nombre', 'precio', 'descripcion', 'imagen']
    success_url = reverse_lazy('productos_list') 


class ProductoUpdateView(LoginRequiredMixin, UpdateView):
    model = Producto
    template_name = 'core/producto_form.html'
    fields = ['nombre', 'precio', 'descripcion', 'imagen']
    success_url = reverse_lazy('productos_list')


class ProductoDeleteView(LoginRequiredMixin, DeleteView):
    model = Producto
    template_name = 'core/producto_confirm_delete.html'
    success_url = reverse_lazy('productos_list')