from django.test import TestCase
from django.contrib.auth.models import User
from .models import Usuario

class UsuarioModelTest(TestCase):
    def test_crear_usuario(self):
        user = User.objects.create_user(username='testuser', email='testuser@example.com', password='password')
        usuario = Usuario.objects.create(user=user, telefono='123456789')
        self.assertEqual(usuario.user.username, 'testuser')
