# ventas/forms.py

from django import forms
from django.forms import inlineformset_factory
from .models import Venta
from clientes.models import Cliente
from productos.models import ProductoVenta, ProductoAlquiler
from pedidos.models import Pedido, PedidoProducto
from pagos.models import Pago
from sesiones_fotos.models import SesionFoto
from django_select2.forms import Select2Widget, ModelSelect2MultipleWidget
from pedidos.forms import PedidoProductoForm

class DateInput(forms.DateInput):
    input_type = 'date'

class VentaForm(forms.ModelForm):
    cliente = forms.ModelChoiceField(
        queryset=Cliente.objects.all(),
        widget=Select2Widget
    )

    class Meta:
        model = Venta
        exclude = ['id_venta', 'created_by', 'creation_date', 'changetimestamp', 'total_a_pagar', 'pendiente_de_pago']
        widgets = {
            'fecha_entrega': DateInput(),
            'fecha_devolucion': DateInput(),
        }

class ProductoVentaInlineForm(forms.ModelForm):
    class Meta:
        model = ProductoVenta
        fields = ['nombre']

class ProductoAlquilerInlineForm(forms.ModelForm):
    class Meta:
        model = ProductoAlquiler
        fields = ['nombre']

class SesionFotoInlineForm(forms.ModelForm):
    class Meta:
        model = SesionFoto
        fields = ['producto']

class PagoForm(forms.ModelForm):
    class Meta:
        model = Pago
        fields = ['importe', 'metodo_pago']

PagoFormSet = inlineformset_factory(Venta, Pago, form=PagoForm, extra=1)
ProductoVentaFormSet = inlineformset_factory(Venta, ProductoVenta, form=ProductoVentaInlineForm, extra=1, can_delete=True)
ProductoAlquilerFormSet = inlineformset_factory(Venta, ProductoAlquiler, form=ProductoAlquilerInlineForm, extra=1, can_delete=True)
PedidoProductoFormSet = inlineformset_factory(Pedido, PedidoProducto, form=PedidoProductoForm, extra=1, can_delete=True)
SesionFotoFormSet = inlineformset_factory(Venta, SesionFoto, form=SesionFotoInlineForm, extra=1, can_delete=True)
