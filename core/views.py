from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
# Imports para Vistas Basadas en Clases (CBV) y Mixins de Seguridad
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

# Importar Modelos y Formularios
from .models import Pedido, Producto, PedidoProducto, Perfil
from .forms import RegistroUsuarioForm, UserEditForm, PerfilForm, ProductoForm

# --- VISTAS GENERALES ---

@login_required
def home(request):
    pedidos = Pedido.objects.filter(cliente=request.user)
    return render(request, 'core/home.html', {'pedidos': pedidos})

def about(request):
    return render(request, 'core/about.html')

# --- AUTENTICACIÓN Y PERFIL ---

def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Registro exitoso! Ya puedes iniciar sesión.')
            return redirect('login')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'core/registro.html', {'form': form})

@login_required
def mi_perfil(request):
    # Crear perfil si no existe (seguridad para usuarios viejos)
    perfil, created = Perfil.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=request.user)
        perfil_form = PerfilForm(request.POST, request.FILES, instance=perfil)
        
        if user_form.is_valid() and perfil_form.is_valid():
            user_form.save()
            perfil_form.save()
            messages.success(request, 'Tu perfil ha sido actualizado.')
            return redirect('mi_perfil')
    else:
        user_form = UserEditForm(instance=request.user)
        perfil_form = PerfilForm(instance=perfil)

    context = {
        'user_form': user_form,
        'perfil_form': perfil_form,
        'perfil': perfil
    }
    return render(request, 'core/perfil.html', context)

# --- SISTEMA DE PEDIDOS (Lógica original) ---

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
    item = get_object_or_404(PedidoProducto, id=item_id, pedido__cliente=request.user)
    pedido_id = item.pedido.id
    item.delete()
    return redirect('detalle_pedido', pedido_id)

# --- CRUD DE PRODUCTOS / MENÚ (Protegido para Admin) ---

# LIST VIEW: Visible para todos (para que puedan pedir), pero podríamos restringirlo si quisieras
class ProductoListView(ListView):
    model = Producto
    template_name = 'core/productos_list.html'
    context_object_name = 'productos'

# CREATE VIEW: Solo para Staff (Admin)
class ProductoCreateView(UserPassesTestMixin, CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'core/producto_form.html'
    success_url = reverse_lazy('productos_list')

    # Verificación de seguridad
    def test_func(self):
        return self.request.user.is_staff

# UPDATE VIEW: Solo para Staff (Admin)
class ProductoUpdateView(UserPassesTestMixin, UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'core/producto_form.html'
    success_url = reverse_lazy('productos_list')

    def test_func(self):
        return self.request.user.is_staff

# DELETE VIEW: Solo para Staff (Admin)
class ProductoDeleteView(UserPassesTestMixin, DeleteView):
    model = Producto
    template_name = 'core/producto_confirm_delete.html'
    success_url = reverse_lazy('productos_list')

    def test_func(self):
        return self.request.user.is_staff