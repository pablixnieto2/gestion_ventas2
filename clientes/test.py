from django.test import TestCase
from .models import Cliente

class ClienteModelTest(TestCase):
    def test_crear_cliente(self):
        cliente = Cliente.objects.create(
            created_by="test@example.com",
            nombre="Test",
            apellido="User",
            telefono="123456789",
            email="test@example.com"
        )
        self.assertEqual(cliente.nombre, "Test")
