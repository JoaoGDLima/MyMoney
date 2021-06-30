from django.test import TestCase
from ..models import Categoria
from ..models import Lancamento
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
    
    def test_retorno_tipo_categoria(self):
        c1 = Categoria.objects.get(nome='Alimentação')
        self.assertEquals(c1.tipo, 'D')

    def test_retorno_usuario(self):
        c1 = Categoria.objects.get(nome='Alimentação')
        self.assertEquals(c1.usuario.username, 'test')


class LancamentoTestCase(TestCase):
    def setUp(self):
        # criando usuário
        test_user1 = get_user_model().objects.create_user(username='test', password='123', email='test@test.com')
        test_user1.save()

        categoria = Categoria.objects.create(
            nome = "Alimentação",
            tipo = "D",
            usuario = test_user1
        )

        # criando lançamento
        Lancamento.objects.create(
            tipo = "D",
            valor = 5.0,
            usuario = test_user1,
            observacao = "teste",
            categoria = categoria
        )
    
    def test_retorno_observacao_lancamento(self):
        l1 = Lancamento.objects.get(observacao = 'teste')
        self.assertEquals(l1.__str__(), 'teste')
    
    def test_retorno_valor_lancamento(self):
        l1 = Lancamento.objects.get(observacao = 'teste')
        self.assertEquals(l1.valor, 5.0)

    def test_retorno_tipo_lancamento(self):
        l1 = Lancamento.objects.get(observacao = 'teste')
        self.assertEquals(l1.tipo, 'D')
    
    def test_retorno_categoria_lancamento(self):
        l1 = Lancamento.objects.get(observacao = 'teste')
        self.assertEquals(l1.categoria.nome, 'Alimentação')
    
    def test_retorno_usuario_lancamento(self):
        l1 = Lancamento.objects.get(observacao = 'teste')s
        self.assertEquals(l1.usuario.username, 'test')