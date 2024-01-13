from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

from .forms import (
    RegistroForm, PedidoForm, ElementoPedidoForm,
    ProductoForm, ProveedorForm
)
from .models import (
    ElementoPedido, Pedido, HistorialPedido,
    Producto, Proveedor, SeguimientoPedido, TablaAuxiliar1
)

# Función auxiliar para verificar si un usuario es un superusuario
def is_superuser(user):
    return user.is_superuser

# Función auxiliar para verificar si un usuario tiene ciertos permisos
def has_custom_permission(user):
    # Agrega aquí lógica para verificar los permisos específicos
    return user.has_perm('app.custom_permission')

# Decorador para requerir inicio de sesión
@login_required
def inicio(request):
    return render(request, 'farmacia_app/inicio.html')

# Decorador para requerir inicio de sesión y verificar permisos personalizados
@user_passes_test(has_custom_permission)
def funcion_con_permisos_personalizados(request):
    # Código de la vista
    pass

# Decorador para requerir inicio de sesión y verificar superusuario
@user_passes_test(is_superuser)
def funcion_solo_superusuario(request):
    # Código de la vista
    pass

# Funciones originales
@login_required
def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('inicio')
    else:
        form = RegistroForm()
    return render(request, 'farmacia_app/registro.html', {'form': form})

@login_required
def inicio(request):
    return render(request, 'farmacia_app/inicio.html')

def inicio_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('sesion_iniciada')
    else:
        form = AuthenticationForm()
    return render(request, 'farmacia_app/inicio_sesion.html', {'form': form})

@login_required
def sesion_iniciada(request):
    return render(request, 'farmacia_app/inicio_sesion.html')

@login_required
def crear_pedido(request):
    if request.method == 'POST':
        form_pedido = PedidoForm(request.POST)
        form_elemento = ElementoPedidoForm(request.POST)

        if form_pedido.is_valid() and form_elemento.is_valid():
            # Guardar el pedido
            pedido = form_pedido.save()

            # Guardar el elemento del pedido asociado al pedido
            elemento_pedido = form_elemento.save(commit=False)
            elemento_pedido.pedido = pedido
            elemento_pedido.save()

            return redirect('lista_pedidos')

    else:
        form_pedido = PedidoForm()
        form_elemento = ElementoPedidoForm()

    return render(request, 'farmacia_app/crear_pedido.html', {'form_pedido': form_pedido, 'form_elemento': form_elemento})

@login_required
def ver_pedido(request):
    historial_pedidos = HistorialPedido.objects.filter(cliente=request.user)
    return render(request, 'farmacia_app/ver_pedido.html', {'historial_pedidos': historial_pedidos})

@login_required
def historial_pedidos(request):
    historial_pedidos = HistorialPedido.objects.filter(cliente=request.user)
    return render(request, 'historial_pedidos.html', {'historial_pedidos': historial_pedidos})

# Nuevas funciones para gestionar productos y proveedores
@login_required
def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'listar_productos.html', {'productos': productos})

@login_required
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm()
    return render(request, 'agregar_producto.html', {'form': form})

@login_required
def listar_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'listar_proveedores.html', {'proveedores': proveedores})

@login_required
def agregar_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_proveedores')
    else:
        form = ProveedorForm()
    return render(request, 'agregar_proveedor.html', {'form': form})

@login_required
def tomar_pedido(request):
    if request.method == 'POST':
        form_pedido = PedidoForm(request.POST)
        form_elemento = ElementoPedidoForm(request.POST)

        if form_pedido.is_valid() and form_elemento.is_valid():
            # Guardar el pedido
            pedido = form_pedido.save()

            # Guardar el elemento del pedido asociado al pedido
            elemento_pedido = form_elemento.save(commit=False)
            elemento_pedido.pedido = pedido
            elemento_pedido.save()

            return redirect('lista_pedidos')

    else:
        form_pedido = PedidoForm()
        form_elemento = ElementoPedidoForm()
    return render(request, 'farmacia_app/tomar_pedido.html', {'form_pedido': form_pedido, 'form_elemento': form_elemento})

def seguimiento_pedidos(request, pedido_id):
    seguimientos = SeguimientoPedido.objects.filter(pedido_id=pedido_id)
    return render(request, 'farmacia_app/seguimiento_pedidos.html', {'seguimientos': seguimientos})

@login_required
def listar_tabla_auxiliar1(request):
    registros = TablaAuxiliar1.objects.all()
    return render(request, 'listar_tabla_auxiliar1.html', {'registros': registros})

@login_required
def agregar_tabla_auxiliar1(request):
    if request.method == 'POST':

        return redirect('listar_tabla_auxiliar1')
    else:
        return render(request, 'agregar_tabla_auxiliar1.html')

@user_passes_test(is_superuser)
def listar_tabla_auxiliar1(request):
    registros = TablaAuxiliar1.objects.all()
    return render(request, 'listar_tabla_auxiliar1.html', {'registros': registros})

@user_passes_test(is_superuser)
def agregar_tabla_auxiliar1(request):
    if request.method == 'POST':
        # Procesar formulario y guardar registro en TablaAuxiliar1
        return redirect('listar_tabla_auxiliar1')
    else:
        # Mostrar formulario para agregar registro en TablaAuxiliar1
        return render(request, 'agregar_tabla_auxiliar1.html')