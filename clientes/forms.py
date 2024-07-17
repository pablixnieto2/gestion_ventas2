from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'estado_cliente', 'ubicacion', 'nombre', 'apellido', 'prefijo', 'telefono', 'email','fecha_fiesta',
            'como_nos_conocio', 'comentarios', 'codigo_postal', 'vendedora',
        ]
        widgets = {
            'ubicacion': forms.Select(choices=Cliente.UBICACION_CHOICES),
            'estado': forms.Select(choices=Cliente.ESTADO_CHOICES),
            'como_nos_conocio': forms.Select(choices=Cliente.COMO_NOS_CONOCIO_CHOICES),
            'estado_cliente': forms.Select(choices=Cliente.ESTADO_CLIENTE_CHOICES),
        }
