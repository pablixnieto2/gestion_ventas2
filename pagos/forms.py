# pagos/forms.py

from django import forms
from .models import Pago

class DateInput(forms.DateInput):
    input_type = 'date'

class PagoForm(forms.ModelForm):
    class Meta:
        model = Pago
        fields = [
            'venta', 'cantidad', 'metodo_pago', 'comentarios', 'estado_pago'
        ]
        widgets = {
            'creation_date': DateInput(),
        }
