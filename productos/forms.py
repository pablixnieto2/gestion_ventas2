# productos/forms.py

from django import forms
from .models import ProductoVenta, ProductoAlquiler

class ProductoVentaForm(forms.ModelForm):
    class Meta:
        model = ProductoVenta
        fields = [
            'categoria', 'nombre', 'color', 'talla', 'pvp', 'image', 
            'estado', 'tienda', 'stock'
        ]
        widgets = {
            'categoria': forms.Select(choices=ProductoVenta.CATEGORIA_CHOICES),
            'estado': forms.Select(choices=ProductoVenta.ESTADO_CHOICES),
            'tienda': forms.Select(choices=ProductoVenta.TIENDA_CHOICES),
        }

class ProductoAlquilerForm(forms.ModelForm):
    class Meta:
        model = ProductoAlquiler
        fields = [
            'categoria', 'nombre', 'color', 'talla', 'pvp', 'image', 
            'estado', 'tienda', 'cantidad'
        ]
        widgets = {
            'categoria': forms.Select(choices=ProductoAlquiler.CATEGORIA_CHOICES),
            'estado': forms.Select(choices=ProductoAlquiler.ESTADO_CHOICES),
            'tienda': forms.Select(choices=ProductoAlquiler.TIENDA_CHOICES),
        }
