from django import forms
from .models import Pago

class PagoForm(forms.ModelForm):
    class Meta:
        model = Pago
        fields = [
            'id_pago', 'venta', 'created_by', 'creation_date', 'cantidad', 'metodo_pago',
            'referencia_pago', 'comentarios', 'estado_pago'
        ]
        widgets = {
            'creation_date': forms.DateInput(attrs={'type': 'date'}),
            'metodo_pago': forms.Select(choices=[
                ('Efectivo', 'Efectivo'),
                ('Tarjeta', 'Tarjeta'),
                ('Transferencia', 'Transferencia'),
                ('Paypal', 'Paypal')
            ]),
            'estado_pago': forms.Select(choices=[
                ('Pendiente', 'Pendiente'),
                ('Pagado', 'Pagado'),
                ('Reembolsado', 'Reembolsado')
            ]),
        }
