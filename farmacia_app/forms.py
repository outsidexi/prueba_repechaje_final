from django import forms
from .models import Usuario, Producto, Pedido, ElementoPedido, Proveedor

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'nombre_completo', 'password']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'proveedor']

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente', 'direccion_entrega', 'fecha_entrega']

class ElementoPedidoForm(forms.ModelForm):
    class Meta:
        model = ElementoPedido
        fields = ['producto', 'cantidad', 'precio']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['producto'].queryset = Producto.objects.all()

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'direccion', 'telefono']

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente', 'direccion_entrega', 'fecha_entrega']

class ElementoPedidoForm(forms.ModelForm):
    class Meta:
        model = ElementoPedido
        fields = ['producto', 'cantidad', 'precio']