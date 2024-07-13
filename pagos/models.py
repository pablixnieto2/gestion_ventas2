from django.db import models
from django.utils import timezone
from ventas.models import Venta

class Pago(models.Model):
    id_pago = models.CharField(max_length=6, unique=True, primary_key=True)
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    created_by = models.EmailField()
    creation_date = models.DateTimeField(default=timezone.now)
    changetimestamp = models.DateTimeField(auto_now=True)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.CharField(max_length=50, choices=[
        ('Efectivo', 'Efectivo'),
        ('Tarjeta', 'Tarjeta'),
        ('Transferencia', 'Transferencia'),
        ('Paypal', 'Paypal')
    ])
    referencia_pago = models.CharField(max_length=50, blank=True, null=True)
    comentarios = models.TextField(blank=True)
    estado_pago = models.CharField(max_length=50, choices=[
        ('Pendiente', 'Pendiente'),
        ('Pagado', 'Pagado'),
        ('Reembolsado', 'Reembolsado')
    ])

    def __str__(self):
        return f"{self.id_pago} - {self.venta.id_venta}"

    class Meta:
        verbose_name_plural = "Pagos"
