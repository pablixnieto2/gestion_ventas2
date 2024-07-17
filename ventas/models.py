# ventas/models.py

from django.db import models
from django.utils import timezone
from clientes.models import Cliente
from productos.models import Producto

class Venta(models.Model):
    TIENDA_CHOICES = [
        ('Madrid', 'Madrid'),
        ('Barcelona', 'Barcelona'),
        ('Valencia', 'Valencia'),
        ('Videollamada', 'Videollamada')
    ]
    ESTADO_ENTREGA_CHOICES = [
        ('Por Entregar o Enviar', 'Por Entregar o Enviar'),
        ('Entregado o Enviado', 'Entregado o Enviado'),
        ('Vestido Devuelto', 'Vestido Devuelto')
    ]
    TIPO_CHOICES = [
        ('Alquiler', 'Alquiler'),
        ('Venta', 'Venta')
    ]
    ESTADO_DEPOSITO_CHOICES = [
        ('Pendiente de Entrega', 'Pendiente de Entrega'),
        ('Entregado por el Cliente', 'Entregado por el Cliente'),
        ('Devuelto al Cliente', 'Devuelto al Cliente')
    ]

    id_venta = models.CharField(max_length=6, unique=True, primary_key=True)
    created_by = models.EmailField()
    creation_date = models.DateTimeField(default=timezone.now)
    changetimestamp = models.DateTimeField(auto_now=True)
    tienda = models.CharField(max_length=50, choices=TIENDA_CHOICES, default='Madrid')
    envio_entrega = models.BooleanField(default=False)
    estado_entrega = models.CharField(max_length=50, choices=ESTADO_ENTREGA_CHOICES, default='Por Entregar o Enviar')
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES, default='Venta')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto)
    fecha_entrega = models.DateField()
    fecha_devolucion = models.DateField(blank=True, null=True)
    amount_deposito = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    estado_deposito = models.CharField(max_length=50, choices=ESTADO_DEPOSITO_CHOICES, blank=True, null=True)
    direccion = models.TextField(blank=True)
    precio_envio = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_a_pagar = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_pagado = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    pendiente_de_pago = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    estado_pago = models.CharField(max_length=50, default='Pendiente')  # Definir valor predeterminado
    comentarios = models.TextField(blank=True)
    estado_venta = models.CharField(max_length=50, default='En Proceso')  # Definir valor predeterminado
    descuento = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    motivo = models.TextField(blank=True)
    devolucion = models.TextField(blank=True)
    pdf = models.FileField(upload_to='ventas/pdfs/', blank=True, null=True)

    def save(self, *args, **kwargs):
        self.total_a_pagar = sum(producto.pvp for producto in self.productos.all()) + self.precio_envio - self.descuento
        self.pendiente_de_pago = self.total_a_pagar - self.total_pagado
        if self.total_pagado == 0:
            self.estado_pago = "Incluir Pago"
        elif self.total_pagado < 0:
            self.estado_pago = "Revisar Venta"
        elif self.pendiente_de_pago > 0:
            self.estado_pago = "Pagado Parcialmente"
        elif self.pendiente_de_pago == 0:
            self.estado_pago = "Pagado"
        else:
            self.estado_pago = "Devolver al Cliente"

        if "Cancel" in self.comentarios:
            self.estado_venta = "Cancelada"
        elif self.estado_deposito == "Pendiente de Entrega" or self.estado_pago == "Pagado Parcialmente" or (self.tipo == "Alquiler" and self.estado_entrega == "Entregado o Enviado"):
            self.estado_venta = "En Proceso"
        elif self.tipo == "Venta" and self.estado_entrega == "Entregado o Enviado" and self.estado_pago == "Pagado":
            self.estado_venta = "Completa"
        elif self.tipo == "Alquiler" and self.estado_entrega == "Vestido Devuelto" and self.estado_pago == "Pagado":
            self.estado_venta = "Completa"
        else:
            self.estado_venta = "En Proceso"

        super().save(*args, **kwargs)

    def __str__(self):
        return self.id_venta

    class Meta:
        verbose_name_plural = "Ventas"

class Pago(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='ventas_pagos')  # Cambia el related_name aquí
    fecha = models.DateField(default=timezone.now)
    importe = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.fecha} - {self.importe}"

    class Meta:
        verbose_name_plural = "Pagos"