from django.db import models
from django.utils import timezone

class Producto(models.Model):
    id_producto = models.CharField(max_length=6, unique=True, primary_key=True)
    label_precio = models.CharField(max_length=255, blank=True)
    almacen_m = models.IntegerField(default=0)
    madrid = models.IntegerField(default=0)
    barcelona = models.IntegerField(default=0)
    tienda = models.CharField(max_length=50, choices=[
        ('Madrid', 'Madrid'),
        ('Barcelona', 'Barcelona'),
        ('Valencia', 'Valencia'),
        ('Videollamada', 'Videollamada')
    ])
    categoria = models.CharField(max_length=50, choices=[
        ('Vestido', 'Vestido'),
        ('Vestido Corto', 'Vestido Corto'),
        ('Accesorios', 'Accesorios'),
        ('Complementos', 'Complementos'),
        ('Envio', 'Envio'),
        ('Invitaciones', 'Invitaciones'),
        ('Paquete Fotos', 'Paquete Fotos'),
        ('Recuerdos', 'Recuerdos'),
        ('Otros', 'Otros')
    ])
    nombre = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    talla = models.CharField(max_length=10)
    pvp = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='productos/', blank=True, null=True)
    estado = models.CharField(max_length=10, choices=[
        ('Activo', 'Activo'),
        ('Baja', 'Baja')
    ])
    tipo = models.CharField(max_length=10, choices=[
        ('Venta', 'Venta'),
        ('Alquiler', 'Alquiler')
    ])

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
