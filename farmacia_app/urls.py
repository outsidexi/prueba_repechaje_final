from django.urls import path
from .views import (
    registro, inicio, inicio_sesion, sesion_iniciada,
    crear_pedido, ver_pedido, historial_pedidos,
    listar_productos, agregar_producto, listar_proveedores, agregar_proveedor, tomar_pedido, seguimiento_pedidos
)

urlpatterns = [
    path('', inicio, name='raiz'),  
    path('registro/', registro, name='registro'),
    path('inicio/', inicio, name='inicio'),
    path('inicio_sesion/', inicio_sesion, name='inicio_sesion'),
    path('sesion_iniciada/', sesion_iniciada, name='sesion_iniciada'),

    # Rutas relacionadas con los pedidos
    path('crear_pedido/', crear_pedido, name='crear_pedido'),
    path('ver_pedido/<int:id_pedido>/', ver_pedido, name='ver_pedido'),
    path('historial-pedidos/', historial_pedidos, name='historial_pedidos'),

    # Rutas relacionadas con productos y proveedores
    path('productos/', listar_productos, name='listar_productos'),
    path('productos/agregar/', agregar_producto, name='agregar_producto'),
    path('proveedores/', listar_proveedores, name='listar_proveedores'),
    path('proveedores/agregar/', agregar_proveedor, name='agregar_proveedor'),
 
    # Ruta para tomar pedidos
    path('tomar_pedido/', tomar_pedido, name='tomar_pedido'),
    path('seguimiento_pedidos/<int:pedido_id>/', seguimiento_pedidos, name='seguimiento_pedidos'),
]
