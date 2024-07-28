# pedidos/forms.py

from django import forms
from django.forms import inlineformset_factory
from .models import Pedido, PedidoProducto
from productos.models import ProductoVenta

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente', 'estado_pedido', 'comentarios']

class PedidoProductoForm(forms.ModelForm):
    class Meta:
        model = PedidoProducto
        fields = ['producto', 'cantidad', 'precio_unitario']
        widgets = {
            'precio_unitario': forms.TextInput(attrs={'readonly': 'readonly'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['producto'].queryset = ProductoVenta.objects.filter(categoria='Recuerdos')
        self.fields['producto'].widget.attrs.update({
            'onchange': 'updatePriceUnitario(this)'
        })

PedidoProductoFormSet = inlineformset_factory(Pedido, PedidoProducto, form=PedidoProductoForm, extra=1)
