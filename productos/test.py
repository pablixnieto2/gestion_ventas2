from django.test import TestCase
from .models import ProductoVenta, ProductoAlquiler

class ProductoModelTest(TestCase):
    def test_crear_producto_venta(self):
        producto = ProductoVenta.objects.create(
            id_producto="P0001",
            nombre="Vestido",
            categoria="Vestido",
            color="Rojo",
            talla="M",
            pvp=100.00,
            estado="Activo",
            stock=10
        )
        self.assertEqual(producto.nombre, "Vestido")

    def test_crear_producto_alquiler(self):
        producto = ProductoAlquiler.objects.create(
            id_producto="A0001",
            nombre="Vestido Alquiler",
            categoria="Vestido",
            color="Azul",
            talla="L",
            precio_alquiler=50.00,
            estado="Activo",
            stock=5
        )
        self.assertEqual(producto.nombre, "Vestido Alquiler")
