import uuid
from django.db import models

class Producto(models.Model):
    id_producto = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    label_precio = models.CharField(max_length=255, blank=True, editable=False)
    madrid = models.IntegerField(default=0)
    barcelona = models.IntegerField(default=0)
    valencia = models.IntegerField(default=0)

    MADRID = 'Madrid'
    BARCELONA = 'Barcelona'
    VALENCIA = 'Valencia'
    VIDEOLLAMADA = 'Videollamada'
    
    TIENDA_CHOICES = [
        (MADRID, 'Madrid'),
        (BARCELONA, 'Barcelona'),
        (VALENCIA, 'Valencia'),
        (VIDEOLLAMADA, 'Videollamada')
    ]
    
    tienda = models.CharField(max_length=50, choices=TIENDA_CHOICES)
    
    VESTIDO = 'Vestido'
    VESTIDO_CORTO = 'Vestido Corto'
    ACCESORIOS = 'Accesorios'
    COMPLEMENTOS = 'Complementos'
    ENVIO = 'Envio'
    INVITACIONES = 'Invitaciones'
    PAQUETE_FOTOS = 'Paquete Fotos'
    RECUERDOS = 'Recuerdos'
    OTROS = 'Otros'
    
    CATEGORIA_CHOICES = [
        (VESTIDO, 'Vestido'),
        (VESTIDO_CORTO, 'Vestido Corto'),
        (ACCESORIOS, 'Accesorios'),
        (COMPLEMENTOS, 'Complementos'),
        (ENVIO, 'Envio'),
        (INVITACIONES, 'Invitaciones'),
        (PAQUETE_FOTOS, 'Paquete Fotos'),
        (RECUERDOS, 'Recuerdos'),
        (OTROS, 'Otros')
    ]
    
    categoria = models.CharField(max_length=50, choices=CATEGORIA_CHOICES)
    nombre = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    talla = models.CharField(max_length=10)
    pvp = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='productos/', blank=True, null=True)
    
    ACTIVO = 'Activo'
    BAJA = 'Baja'
    
    ESTADO_CHOICES = [
        (ACTIVO, 'Activo'),
        (BAJA, 'Baja')
    ]
    
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES)
    
    VENTA = 'Venta'
    ALQUILER = 'Alquiler'
    
    TIPO_CHOICES = [
        (VENTA, 'Venta'),
        (ALQUILER, 'Alquiler')
    ]
    
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)

    @property
    def nombres(self):
        return f"{self.tienda[0]} {self.categoria} {self.nombre} {self.color} {self.talla}"

    @property
    def reservados(self):
        return self.ventas_set.filter(estado_venta='En Proceso').count()

    @property
    def disponibles(self):
        return self.almacen_m + self.madrid + self.barcelona - self.reservados

    def save(self, *args, **kwargs):
        if self.tipo == 'Alquiler':
            self.label_precio = f"{self.tienda[0]} {self.categoria} {self.nombre} {self.color} {self.talla} - {self.pvp} €"
        else:
            self.label_precio = f"{self.categoria} {self.nombre} {self.color} {self.talla} - {self.pvp} €"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Productos"
