from django.db import models
from django.utils import timezone
from clientes.models import Cliente
from ventas.models import Venta
from productos.models import ProductoVenta

class SesionFoto(models.Model):
    ESTADO_SESION_CHOICES = [
        ('Pendiente de confirmar', 'Pendiente de confirmar'),
        ('Confirmada', 'Confirmada'),
        ('En Edición', 'En Edición'),
        ('Pendiente Link', 'Pendiente Link'),
        ('Link Enviado', 'Link Enviado'),
        ('Pendiente Nº Fotos', 'Pendiente Nº Fotos'),
        ('Pendiente Albúm', 'Pendiente Albúm'),
        ('En Espera de Recibir Albúm', 'En Espera de Recibir Albúm'),
        ('Completada', 'Completada'),
        ('Reedición', 'Reedición'),
        ('Cancelada', 'Cancelada')
    ]

    id_sesion = models.CharField(max_length=6, unique=True, primary_key=True)
    created_by = models.EmailField()
    creation_date = models.DateTimeField(default=timezone.now)
    changetimestamp = models.DateTimeField(auto_now=True)
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(ProductoVenta, on_delete=models.CASCADE)
    fecha_sesion = models.DateField()
    duracion = models.DurationField()
    lugar = models.CharField(max_length=100)
    estado_sesion = models.CharField(max_length=50, choices=ESTADO_SESION_CHOICES)
    extras = models.TextField(blank=True)
    fecha_segunda_sesion = models.DateField(null=True, blank=True)
    notas = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return self.id_sesion

    class Meta:
        verbose_name_plural = "Sesiones de Fotos"
