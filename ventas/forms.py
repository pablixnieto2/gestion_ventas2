from django import forms
from .models import Venta, Pago
from django_select2.forms import ModelSelect2MultipleWidget
from django.forms import inlineformset_factory
from productos.models import Producto

class DateInput(forms.DateInput):
    input_type = 'date'

class VentaForm(forms.ModelForm):
    productos = forms.ModelMultipleChoiceField(
        queryset=Producto.objects.filter(estado='Activo'),
        widget=ModelSelect2MultipleWidget(
            model=Producto,
            search_fields=['nombre__icontains', 'categoria__icontains']
        )
    )

    class Meta:
        model = Venta
        exclude = ['changetimestamp', 'total_a_pagar', 'pendiente_de_pago']
        widgets = {
            'fecha_entrega': DateInput(),
            'fecha_devolucion': DateInput(),
        }

class PagoForm(forms.ModelForm):
    class Meta:
        model = Pago
        fields = ['fecha', 'importe']

PagoFormSet = inlineformset_factory(Venta, Pago, form=PagoForm, extra=1)
