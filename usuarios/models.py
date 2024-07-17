from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    rol = models.CharField(max_length=50, choices=[
        ('admin', 'Admin'),
        ('vendedor', 'Vendedor'),
        ('cliente', 'Cliente')
    ], default='cliente')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = "Usuarios"
