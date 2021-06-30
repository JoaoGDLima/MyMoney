from django.db import models
from django.contrib.auth import get_user_model

class Categoria(models.Model):
    TIPOS = (
        ('D', 'Despesas'),
        ('R', 'Receitas'),
    )

    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=31,choices=TIPOS)
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nome

class Lancamento(models.Model):

    TIPOS = (
        ('D', 'Despesas'),
        ('R', 'Receitas'),
    )

    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    datahora = models.DateTimeField(null=False, auto_now_add=True)
    valor = models.FloatField(max_length=10.2)
    tipo = models.CharField(max_length=1,choices=TIPOS)
    observacao = models.CharField(max_length=100,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.observacao

    
class Tipo2(models.Model):
    nome = models.CharField(max_length=100)
