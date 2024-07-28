from django.db import models
from django.utils import timezone
from ventas.models import Venta
from clientes.models import Cliente
from productos.models import Producto

class Pedido(models.Model):
    ESTADO_PEDIDO_CHOICES = [
        ('Pendiente', 'Pendiente'),
        ('Procesando', 'Procesando'),
        ('Completado', 'Completado'),
        ('Cancelado', 'Cancelado')
    ]

    RECUERDOS_CHOICES = [
        ('Cojín', 'Cojín'),
        ('Espejos', 'Espejos'),
        ('Muñecas', 'Muñecas'),
        ('Monedero', 'Monedero'),
        ('Imán', 'Imán'),
        ('Taza', 'Taza'),
        ('Cuadro Foto', 'Cuadro Foto'),
        ('Ramo Personalizado', 'Ramo Personalizado'),
    ]

    COLOR_CHOICES = [
        ('Rosa', 'Rosa'),
        ('Morado', 'Morado'),
        ('Rojo', 'Rojo'),
        ('Rojo Vino', 'Rojo Vino'),
        ('Verde Claro', 'Verde Claro'),
        ('Verde Oscuro', 'Verde Oscuro'),
        ('Turquesa', 'Turquesa'),
        ('Azul Oscuro', 'Azul Oscuro'),
        ('Azul Claro', 'Azul Claro'),
        ('Amarillo', 'Amarillo'),
        ('Negro', 'Negro'),
    ]

    id_pedido = models.CharField(max_length=6, unique=True, primary_key=True)
    created_by = models.EmailField()
    creation_date = models.DateTimeField(default=timezone.now)
    changetimestamp = models.DateTimeField(auto_now=True)
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    recuerdo = models.CharField(max_length=50, choices=RECUERDOS_CHOICES)
    estado_pedido = models.CharField(max_length=50, choices=ESTADO_PEDIDO_CHOICES)
    comentarios = models.TextField(blank=True)
    tienda = models.CharField(max_length=100)
    fecha_entrega = models.DateField()
    nombre_imprimir = models.CharField(max_length=100)
    fecha_imprimir = models.DateField()
    color = models.CharField(max_length=50, choices=COLOR_CHOICES)
    numero_unidades = models.IntegerField(default=1)

    def __str__(self):
        return self.id_pedido

    @property
    def total_a_pagar(self):
        return sum(item.subtotal for item in self.pedidoproducto_set.all())

    class Meta:
        verbose_name_plural = "Pedidos"

class PedidoProducto(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def subtotal(self):
        return self.cantidad * self.precio_unitario

    class Meta:
        verbose_name_plural = "PedidoProductos"
