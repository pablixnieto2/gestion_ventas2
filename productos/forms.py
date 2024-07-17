from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            'valencia', 'madrid', 'barcelona', 'tienda', 
            'categoria', 'nombre', 'color', 'talla', 'pvp', 'image', 
            'estado', 'tipo'
        ]
        widgets = {
            'tienda': forms.Select(choices=Producto.TIENDA_CHOICES),
            'categoria': forms.Select(choices=Producto.CATEGORIA_CHOICES),
            'estado': forms.Select(choices=Producto.ESTADO_CHOICES),
            'tipo': forms.Select(choices=Producto.TIPO_CHOICES),
        }
