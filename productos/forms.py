from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            'id_producto', 'almacen_m', 'madrid', 'barcelona', 'tienda', 'categoria', 'nombre', 
            'color', 'talla', 'pvp', 'image', 'estado', 'tipo'
        ]
        widgets = {
            'tienda': forms.Select(choices=[
                ('Madrid', 'Madrid'),
                ('Valencia', 'Valencia'),
                ('Barcelona', 'Barcelona'),
                ('Videollamada', 'Videollamada')
            ]),
            'categoria': forms.Select(choices=[
                ('Vestido', 'Vestido'),
                ('Vestido Corto', 'Vestido Corto'),
                ('Accesorios', 'Accesorios'),
                ('Complementos', 'Complementos'),
                ('Envio', 'Envio'),
                ('Invitaciones', 'Invitaciones'),
                ('Paquete Fotos', 'Paquete Fotos'),
                ('Recuerdos', 'Recuerdos'),
                ('Otros', 'Otros')
            ]),
            'estado': forms.Select(choices=[
                ('Activo', 'Activo'),
                ('Baja', 'Baja')
            ]),
            'tipo': forms.Select(choices=[
                ('Venta', 'Venta'),
                ('Alquiler', 'Alquiler')
            ])
        }
