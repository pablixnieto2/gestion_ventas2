from django import forms
from .models import Venta
from clientes.models import Cliente
from pagos.models import Pago
from productos.models import ProductoVenta, ProductoAlquiler
from sesiones_fotos.models import SesionFoto
from django_select2.forms import Select2Widget, ModelSelect2MultipleWidget
from django.forms import inlineformset_factory
from pedidos.forms import PedidoProductoFormSet
from sesiones_fotos.forms import SesionFotoForm

class DateInput(forms.DateInput):
    input_type = 'date'

class VentaForm(forms.ModelForm):
    productos_venta = forms.ModelMultipleChoiceField(
        queryset=ProductoVenta.objects.filter(estado='Activo'),
        widget=ModelSelect2MultipleWidget(
            model=ProductoVenta,
            search_fields=['nombre__icontains']
        ),
        required=False
    )

    productos_alquiler = forms.ModelMultipleChoiceField(
        queryset=ProductoAlquiler.objects.filter(estado='Activo'),
        widget=ModelSelect2MultipleWidget(
            model=ProductoAlquiler,
            search_fields=['nombre__icontains']
        ),
        required=False
    )

    cliente = forms.ModelChoiceField(
        queryset=Cliente.objects.all(),
        widget=Select2Widget
    )

    class Meta:
        model = Venta
        exclude = ['id_venta', 'created_by', 'creation_date', 'changetimestamp', 'total_a_pagar', 'pendiente_de_pago']
        widgets = {
            'fecha_entrega': forms.DateInput(attrs={'type': 'date'}),
            'fecha_devolucion': forms.DateInput(attrs={'type': 'date'}),
        }

class PagoForm(forms.ModelForm):
    class Meta: 
        model = Pago
        fields = ['fecha', 'importe']

PagoFormSet = inlineformset_factory(Venta, Pago, form=PagoForm, extra=1)
SesionFotoFormSet = inlineformset_factory(Venta, SesionFoto, form=SesionFotoForm, extra=1)
