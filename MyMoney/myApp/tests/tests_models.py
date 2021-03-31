from django.test import TestCase
from ..models import Categoria
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

class LoginTestCase(TestCase):
    
    def setUp(self):
        # criando usuário
        self.user = get_user_model().objects.create_user(username='test', password='123', email='test@test.com')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_correct(self):
        user = authenticate(username='test', password='123')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_wrong_username(self):
        user = authenticate(username='root', password='123')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_pssword(self):
        user = authenticate(username='test', password='321')
        self.assertFalse(user is not None and user.is_authenticated)


class CategoriaTestCase(TestCase):
    def setUp(self):
        # criando usuário
        test_user1 = get_user_model().objects.create_user(username='test', password='123', email='test@test.com')
        test_user1.save()

        # criando categoria
        Categoria.objects.create(
            nome = "Alimentação",
            tipo = "D",
            usuario = test_user1
        )

    def test_retorno_str(self):
        c1 = Categoria.objects.get(nome='Alimentação')
        self.assertEquals(c1.__str__(), 'Alimentação')

    def test_retorno_usuario(self):
        c1 = Categoria.objects.get(nome='Alimentação')
        self.assertEquals(c1.usuario.username, 'test')