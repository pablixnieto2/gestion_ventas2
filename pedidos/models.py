from django.db import models
from django.utils import timezone
from clientes.models import Cliente
from productos.models import Producto

class Pedido(models.Model):
    id_pedido = models.CharField(max_length=6, unique=True, primary_key=True)
    created_by = models.EmailField()
    creation_date = models.DateTimeField(default=timezone.now)
    changetimestamp = models.DateTimeField(auto_now=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto)
    estado_pedido = models.CharField(max_length=50, choices=[
        ('Pendiente', 'Pendiente'),
        ('Procesando', 'Procesando'),
        ('Completado', 'Completado'),
        ('Cancelado', 'Cancelado')
    ])
    total_a_pagar = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_pagado = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    pendiente_de_pago = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    direccion_envio = models.TextField(blank=True)
    comentarios = models.TextField(blank=True)
    
    def save(self, *args, **kwargs):
        self.total_a_pagar = sum(producto.pvp for producto in self.productos.all())
        self.pendiente_de_pago = self.total_a_pagar - self.total_pagado
        super().save(*args, **kwargs)

    def __str__(self):
        return self.id_pedido

    class Meta:
        verbose_name_plural = "Pedidos"
