from django import forms
from .models import Pedido

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = [
            'id_pedido', 'created_by', 'creation_date', 'cliente', 
            'productos', 'estado_pedido', 'total_a_pagar', 
            'total_pagado', 'pendiente_de_pago', 'direccion_envio', 'comentarios'
        ]
        widgets = {
            'estado_pedido': forms.Select(choices=Pedido.ESTADO_PEDIDO_CHOICES),
        }
