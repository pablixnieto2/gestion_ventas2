from django.db import models
from django.utils import timezone

class Cliente(models.Model):
    id_cliente = models.CharField(max_length=6, unique=True, primary_key=True)
    created_by = models.EmailField()
    creation_date = models.DateTimeField(default=timezone.now)
    fecha_fiesta = models.DateField()
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    prefijo = models.CharField(max_length=3, blank=True, null=True)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
    ubicacion = models.CharField(max_length=50, choices=[
        ('Madrid', 'Madrid'),
        ('Valencia', 'Valencia'),
        ('Barcelona', 'Barcelona'),
        ('Videollamada', 'Videollamada')
    ])
    estado = models.CharField(max_length=50, choices=[
        ('sin cita', 'Sin Cita'),
        ('con cita', 'Con Cita'),
        ('perdido', 'Perdido'),
        ('eliminar cliente duplicado', 'Eliminar Cliente Duplicado')
    ])
    como_nos_conocio = models.CharField(max_length=50, choices=[
        ('Google', 'Google'),
        ('Google maps', 'Google Maps'),
        ('Instagram', 'Instagram'),
        ('Facebook', 'Facebook'),
        ('Recomendación', 'Recomendación'),
        ('Milanuncios', 'Milanuncios'),
        ('Web', 'Web'),
        ('Otro', 'Otro')
    ])
    label_cliente = models.CharField(max_length=255, blank=True)
    whatsapp = models.URLField(blank=True)
    comentarios = models.TextField(blank=True)
    razon_perdida = models.TextField(blank=True)
    codigo_postal = models.CharField(max_length=10, blank=True)
    vendedora = models.CharField(max_length=100, blank=True)
    estado_cliente = models.CharField(max_length=50, choices=[
        ('ya compró', 'Ya Compró'),
        ('perdido', 'Perdido')
    ])

    def save(self, *args, **kwargs):
        self.label_cliente = f"{self.nombre} {self.apellido} - {self.telefono}"
        self.whatsapp = f"http://wa.me/{self.telefono}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.label_cliente

    class Meta:
        verbose_name_plural = "Clientes"
