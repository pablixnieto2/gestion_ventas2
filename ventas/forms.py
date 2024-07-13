from django import forms
from .models import Venta

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = [
            'id_venta', 'created_by', 'creation_date', 'tienda', 'envio_entrega', 'estado_entrega',
            'tipo', 'cliente', 'productos', 'fecha_entrega', 'fecha_devolucion', 'amount_deposito',
            'estado_deposito', 'direccion', 'precio_envio', 'total_a_pagar', 'total_pagado',
            'pendiente_de_pago', 'estado_pago', 'comentarios', 'estado_venta', 'descuento',
            'motivo', 'devolucion', 'pdf', 'identificacion', 'identificacion_trasera', 'coste_fotos',
            'tiara', 'fecha_extra_fotos', 'compras'
        ]
        widgets = {
            'creation_date': forms.DateInput(attrs={'type': 'date'}),
            'fecha_entrega': forms.DateInput(attrs={'type': 'date'}),
            'fecha_devolucion': forms.DateInput(attrs={'type': 'date'}),
            'tienda': forms.Select(choices=[
                ('Madrid', 'Madrid'),
                ('Valencia', 'Valencia'),
                ('Barcelona', 'Barcelona'),
                ('Videollamada', 'Videollamada')
            ]),
            'estado_entrega': forms.Select(choices=[
                ('Por Entregar o Enviar', 'Por Entregar o Enviar'),
                ('Entregado o Enviado', 'Entregado o Enviado'),
                ('Vestido Devuelto', 'Vestido Devuelto')
            ]),
            'tipo': forms.Select(choices=[
                ('Alquiler', 'Alquiler'),
                ('Venta', 'Venta')
            ]),
            'estado_deposito': forms.Select(choices=[
                ('Pendiente de Entrega', 'Pendiente de Entrega'),
                ('Entregado por el Cliente', 'Entregado por el Cliente'),
                ('Devuelto al Cliente', 'Devuelto al Cliente')
            ]),
            'tiara': forms.Select(choices=[
                ('Entregada', 'Entregada'),
                ('No entregada', 'No entregada'),
                ('Sin tiara', 'Sin tiara')
            ]),
            'fecha_extra_fotos': forms.DateInput(attrs={'type': 'date'}),
        }
