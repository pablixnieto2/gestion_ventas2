from django.db import models
import uuid
from django.utils import timezone

class Producto(models.Model):
    id_producto = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    created_by = models.EmailField()
    creation_date = models.DateTimeField(default=timezone.now)
    
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
    descripcion = models.CharField(max_length=255, blank=True)

    ACTIVO = 'Activo'
    BAJA = 'Baja'
    
    ESTADO_CHOICES = [
        (ACTIVO, 'Activo'),
        (BAJA, 'Baja')
    ]
    
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES)
    
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Productos"

    def generar_descripcion(self):
        self.descripcion = f"{self.categoria} {self.nombre} {self.color} {self.talla} - {self.pvp}€"

    def save(self, *args, **kwargs):
        self.generar_descripcion()
        super().save(*args, **kwargs)

class ProductoVenta(Producto):
    MADRID = 'Madrid'
    BARCELONA = 'Barcelona'
    TIENDA_CHOICES = [
        (MADRID, 'Madrid'),
        (BARCELONA, 'Barcelona')
    ]
    
    tienda = models.CharField(max_length=50, choices=TIENDA_CHOICES)
    stock = models.IntegerField(default=0)
    
    @property
    def disponibles(self):
        return self.stock - self.ventas_set.filter(estado_venta='En Proceso').count()

    class Meta:
        verbose_name_plural = "Productos de Venta"

class ProductoAlquiler(Producto):
    MADRID = 'Madrid'
    BARCELONA = 'Barcelona'
    TIENDA_CHOICES = [
        (MADRID, 'Madrid'),
        (BARCELONA, 'Barcelona')
    ]
    
    tienda = models.CharField(max_length=50, choices=TIENDA_CHOICES)
    cantidad = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Productos de Alquiler"

class Alquiler(models.Model):
    producto = models.ForeignKey(ProductoAlquiler, on_delete=models.CASCADE)
    tienda = models.CharField(max_length=50, choices=ProductoAlquiler.TIENDA_CHOICES)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    unidades = models.IntegerField()

    def __str__(self):
        return f"Alquiler de {self.producto.nombre} en {self.tienda} del {self.fecha_inicio} al {self.fecha_fin}"

def consultar_disponibilidad(producto, tienda, fecha_inicio, fecha_fin):
    disponibilidad = producto.cantidad
    alquileres = Alquiler.objects.filter(
        producto=producto,
        tienda=tienda,
        fecha_inicio__lt=fecha_fin,
        fecha_fin__gt=fecha_inicio
    ).aggregate(total_alquiladas=models.Sum('unidades'))['total_alquiladas'] or 0
    unidades_disponibles = disponibilidad - alquileres
    return unidades_disponibles
