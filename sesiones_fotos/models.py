from django.db import models
from django.utils import timezone
from clientes.models import Cliente

class SesionFoto(models.Model):
    id_sesion = models.CharField(max_length=6, unique=True, primary_key=True)
    created_by = models.EmailField()
    creation_date = models.DateTimeField(default=timezone.now)
    changetimestamp = models.DateTimeField(auto_now=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_sesion = models.DateField()
    lugar = models.CharField(max_length=100)
    estado_sesion = models.CharField(max_length=50, choices=[
        ('Pendiente', 'Pendiente'),
        ('Completada', 'Completada'),
        ('Cancelada', 'Cancelada')
    ])
    comentarios = models.TextField(blank=True)
    fotos_entregadas = models.BooleanField(default=False)
    num_fotos = models.IntegerField(default=0)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_pagado = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    pendiente_de_pago = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    def save(self, *args, **kwargs):
        self.pendiente_de_pago = self.precio - self.total_pagado
        super().save(*args, **kwargs)

    def __str__(self):
        return self.id_sesion

    class Meta:
        verbose_name_plural = "Sesiones de Fotos"
