from django.urls import path
from . import views

urlpatterns = [
    path('helloworld/', views.helloWorld),
    path('', views.accountList, name='account-list'),
    path('categorias/', views.categoryList, name='category-list'),
    path('categoria/<int:id>', views.categoryView, name='category-view'),    
    path('editarCategoria/<int:id>', views.editCategory, name='edit-category'),   
    path('deletarCategoria/<int:id>', views.deleteCategory, name='delete-category'),
    path('novaCategoria/', views.newCategory, name='new-category'),    
]
