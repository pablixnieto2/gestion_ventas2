from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Usuario

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ('username', 'email', 'telefono')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = ('username', 'email', 'telefono')
