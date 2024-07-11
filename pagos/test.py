from django.test import TestCase
from .models import Pago

class PagoModelTest(TestCase):
    def test_crear_pago(self):
        pago = Pago.objects.create(
            id_pago="P0001",
            id_ventas_id=1,  # Assuming you have a Venta instance with id 1
            created_by="test@example.com",
            tienda="Madrid",
            metodo_de_pago="Efectivo",
            importe=100.00
        )
        self.assertEqual(pago.id_pago, "P0001")
