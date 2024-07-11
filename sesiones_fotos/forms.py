from django import forms
from .models import SesionFotos

class SesionFotosForm(forms.ModelForm):
    class Meta:
        model = SesionFotos
        fields = '__all__'
