from django.test import TestCase
from .models import SesionFotos

class SesionFotosModelTest(TestCase):
    def test_crear_sesion_fotos(self):
        sesion = SesionFotos.objects.create(
            id_sesion="S0001",
            venta_id=1,  # Assuming you have a Venta instance with id 1
            fecha_sesion="2023-01-01",
            hora_inicio="10:00:00",
            hora_fin="12:00:00",
            ubicacion="Estudio",
            fotografo="Fotografo Test",
            estado="Pendiente"
        )
        self.assertEqual(sesion.id_sesion, "S0001")
