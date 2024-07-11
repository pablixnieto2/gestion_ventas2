from django.test import TestCase
from .models import Venta

class VentaModelTest(TestCase):
    def test_crear_venta(self):
        venta = Venta.objects.create(
            id_ventas="V0001",
            created_by="test@example.com",
            tienda="Madrid",
            tipo="Venta",
            id_clientes_id=1,  # Assuming you have a Cliente instance with id 1
            fecha_entrega="2023-01-01",
            total_a_pagar=100.00,
            total_pagado=100.00,
            pendiente_de_pago=0.00,
            estado_pago="Pagado"
        )
        self.assertEqual(venta.id_ventas, "V0001")
