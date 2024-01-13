import hashlib
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class Usuario(AbstractUser):
    email = models.EmailField(unique=True)
    nombre_completo = models.CharField(max_length=255)

    groups = models.ManyToManyField(Group, related_name='usuarios')
    user_permissions = models.ManyToManyField(Permission, related_name='usuarios')

    def __str__(self):
        return self.email

    def get_default_password():
        return hashlib.sha256("default_password".encode('utf-8')).hexdigest()

    password = models.CharField(max_length=128, default=get_default_password)

class Proveedor(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    ESTADO_CHOICES = [
        ('en_proceso', 'En Proceso'),
        ('completado', 'Completado'),
        ('cancelado', 'Cancelado'),
    ]
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    direccion_entrega = models.CharField(max_length=255)
    fecha_entrega = models.DateTimeField()
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='en_proceso')

class ElementoPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

class HistorialPedido(models.Model):
    fecha_pedido = models.DateTimeField()
    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    direccion_entrega = models.CharField(max_length=255)
    fecha_entrega = models.DateTimeField()
    estado = models.CharField(max_length=20, choices=Pedido.ESTADO_CHOICES)

class SeguimientoPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    estado = models.CharField(max_length=20)
    ubicacion = models.CharField(max_length=255)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Seguimiento para Pedido {self.pedido.id} - Estado: {self.estado}"
    
class TablaAuxiliar1(models.Model):
    nombre = models.CharField(max_length=255)
  
class TablaAuxiliar2(models.Model):
    nombre = models.CharField(max_length=255)
  