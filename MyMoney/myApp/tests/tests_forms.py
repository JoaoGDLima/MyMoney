from django.test import TestCase
from ..forms import categoryForm
from django.contrib.auth import get_user_model

class CategoriaFormTestCase(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test', password='123', email='test@test.com')
        self.user.save()
        self.user_login = self.client.login(username='test', password='123')
    
    def test_categoria_form_valido(self):
        form =  categoryForm(data={
            'nome': "Teste",
            'tipo': "D"
        })
        self.assertTrue(form.is_valid())

    def test_categoria_form_valido(self):
        form =  categoryForm(data={
            'nome': "Teste",
            'tipo': "D"
        })
        self.assertTrue(form.is_valid())
    
    def test_categoria_form_invalido(self):
        form =  categoryForm(data={})
        self.assertFalse(form.is_valid())
    
    def test_add_categoria(self):
        user_test = get_user_model().objects.create_user(username='test1', password='123', email='test1@test.com')
        form =  categoryForm(data={
            'nome': "Teste",
            'tipo': "D"
        })
        self.assertTrue(form.is_valid())
        categoria = form.save(commit=False)
        self.assertEquals(categoria.nome, "Teste")