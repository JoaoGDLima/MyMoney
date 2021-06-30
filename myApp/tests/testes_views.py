from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

class CategoriaViewTestCase(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test', password='123', email='test@test.com')
        self.user.save()
        self.client.login(username='test', password='123')

    def test_status_code_200(self):
        # simula requisão do navegador
        response = self.client.get(reverse('category-list'))
        self.assertEquals(response.status_code, 200)

    def test_template_list(self):
        # simula requisão do navegador
        response = self.client.get(reverse('category-list'))
        self.assertTemplateUsed(response, 'category/list.html')
    
    def test_template_category_new(self):
        # simula requisão do navegador
        response = self.client.get(reverse('new-category'))
        self.assertTemplateUsed(response, 'category/addCategory.html')

class LancamentoViewTestCase(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test', password='123', email='test@test.com')
        self.user.save()
        self.client.login(username='test', password='123')
    
    def test_account_list_status_code_200(self):
        # simula requisão do navegador
        response = self.client.get(reverse('account-list'))
        self.assertEquals(response.status_code, 200)
    
    def test_template_account_list(self):
        # simula requisão do navegador
        response = self.client.get(reverse('account-list'))
        self.assertTemplateUsed(response, 'account/list.html')

    def test_template_account_new(self):
        # simula requisão do navegador
        response = self.client.get(reverse('new-account'))
        self.assertTemplateUsed(response, 'account/addAccount.html')

