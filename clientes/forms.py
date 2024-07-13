from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'id_cliente', 'created_by', 'creation_date', 'fecha_fiesta', 'nombre', 'apellido', 
            'prefijo', 'telefono', 'email', 'ubicacion', 'estado', 'como_nos_conocio', 
            'comentarios', 'razon_perdida', 'codigo_postal', 'vendedora', 'estado_cliente'
        ]
        widgets = {
            'creation_date': forms.DateInput(attrs={'type': 'date'}),
            'fecha_fiesta': forms.DateInput(attrs={'type': 'date'}),
            'estado': forms.Select(choices=[
                ('sin cita', 'Sin Cita'),
                ('con cita', 'Con Cita'),
                ('perdido', 'Perdido'),
                ('eliminar cliente duplicado', 'Eliminar Cliente Duplicado')
            ]),
            'ubicacion': forms.Select(choices=[
                ('Madrid', 'Madrid'),
                ('Valencia', 'Valencia'),
                ('Barcelona', 'Barcelona'),
                ('Videollamada', 'Videollamada')
            ]),
            'como_nos_conocio': forms.Select(choices=[
                ('Google', 'Google'),
                ('Google maps', 'Google Maps'),
                ('Instagram', 'Instagram'),
                ('Facebook', 'Facebook'),
                ('Recomendación', 'Recomendación'),
                ('Milanuncios', 'Milanuncios'),
                ('Web', 'Web'),
                ('Otro', 'Otro')
            ]),
            'estado_cliente': forms.Select(choices=[
                ('ya compró', 'Ya Compró'),
                ('perdido', 'Perdido')
            ])
        }
