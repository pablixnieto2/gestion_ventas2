from django import forms
from django.forms import inlineformset_factory
from .models import Venta
from clientes.models import Cliente
from pagos.models import Pago
from productos.models import ProductoVenta, ProductoAlquiler
from sesiones_fotos.models import SesionFoto
from django_select2.forms import Select2Widget, ModelSelect2MultipleWidget

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


class SesionFotoForm(forms.ModelForm):
    class Meta:
        model = SesionFoto
        fields = ['cliente', 'venta', 'producto', 'fecha_sesion', 'duracion', 'lugar', 'estado_sesion', 'extras', 'fecha_segunda_sesion', 'notas']
        widgets = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['producto'].queryset = ProductoVenta.objects.filter(categoria='Paquete Fotos')
        self.fields['producto'].widget.attrs.update({
            'onchange': 'updatePriceUnitario(this)'
        })

SesionFotoFormSet = inlineformset_factory(Venta, SesionFoto, form=SesionFotoForm, extra=1)
PagoFormSet = inlineformset_factory(Venta, Pago, form=PagoForm, extra=1)