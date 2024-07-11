from django.test import TestCase
from .models import Pedido

class PedidoModelTest(TestCase):
    def test_crear_pedido(self):
        pedido = Pedido.objects.create(
            id_pedido="P0001",
            id_ventas_id=1,  # Assuming you have a Venta instance with id 1
            proveedor="Proveedor Test",
            fecha_entrega="2023-01-01",
            estado="Pendiente"
        )
        self.assertEqual(pedido.id_pedido, "P0001")
