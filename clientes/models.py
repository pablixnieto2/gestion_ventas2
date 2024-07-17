import uuid
from django.db import models
from django.utils import timezone
from django.urls import reverse

class Cliente(models.Model):
    UBICACION_CHOICES = [
        ('Madrid', 'Madrid'),
        ('Valencia', 'Valencia'),
        ('Barcelona', 'Barcelona'),
        ('Videollamada', 'Videollamada')
    ]
    ESTADO_CHOICES = [
        ('sin cita', 'Sin Cita'),
        ('con cita', 'Con Cita'),
        ('perdido', 'Perdido'),
        ('eliminar cliente duplicado', 'Eliminar Cliente Duplicado')
    ]
    COMO_NOS_CONOCIO_CHOICES = [
        ('Google', 'Google'),
        ('Google maps', 'Google Maps'),
        ('Instagram', 'Instagram'),
        ('Facebook', 'Facebook'),
        ('Recomendación', 'Recomendación'),
        ('Milanuncios', 'Milanuncios'),
        ('Web', 'Web'),
        ('Otro', 'Otro')
    ]
    ESTADO_CLIENTE_CHOICES = [
        ('En Proceso de compra', 'En Proceso de compra'),
        ('ya compró', 'Ya Compró'),
        ('perdido', 'Perdido')
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_by = models.EmailField()
    creation_date = models.DateTimeField(default=timezone.now)
    fecha_fiesta = models.DateField()
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    prefijo = models.CharField(max_length=3, blank=True, null=True)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
    ubicacion = models.CharField(max_length=50, choices=UBICACION_CHOICES)
    estado = models.CharField(max_length=50, choices=ESTADO_CHOICES)
    como_nos_conocio = models.CharField(max_length=50, choices=COMO_NOS_CONOCIO_CHOICES)
    comentarios = models.TextField(blank=True)
    codigo_postal = models.CharField(max_length=10, blank=True)
    vendedora = models.CharField(max_length=100, blank=True)
    estado_cliente = models.CharField(max_length=50, choices=ESTADO_CLIENTE_CHOICES)

    @property
    def duplicados(self):
        return Cliente.objects.filter(email=self.email).exclude(id=self.id).count()

    @property
    def ventas_relacionadas(self):
        return self.venta_set.all()

    @property
    def color(self):
        if self.ubicacion == 'Madrid':
            return 'red'
        elif self.ubicacion == 'Valencia':
            return 'orange'
        elif self.ubicacion == 'Barcelona':
            return 'blue'
        elif self.ubicacion == 'Videollamada':
            return 'green'
        return 'gray'

    @property
    def telefono2(self):
        if self.prefijo:
            return f"+{self.prefijo} {self.telefono}"
        return self.telefono

    @property
    def label_cliente(self):
        return f"{self.nombre} {self.apellido} - {self.telefono}"

    @property
    def whatsapp(self):
        return f"http://wa.me/{self.telefono}"

    @property
    def related_sesiones_fotos(self):
        return self.sesionesfotos_set.all()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('clientes:cliente-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.label_cliente

    class Meta:
        verbose_name_plural = "Clientes"
