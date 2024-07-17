from django import forms
from .models import SesionFoto

class SesionFotoForm(forms.ModelForm):
    class Meta:
        model = SesionFoto
        fields = [
            'id_sesion', 'created_by', 'creation_date', 'cliente', 
            'fecha_sesion', 'lugar', 'estado_sesion', 
            'comentarios', 'fotos_entregadas', 'num_fotos', 'precio', 
            'total_pagado', 'pendiente_de_pago'
        ]
        widgets = {
            'estado_sesion': forms.Select(choices=SesionFoto.ESTADO_SESION_CHOICES),
        }
