from django import forms
from .models import Categoria
from .models import Lancamento

class categoryForm(forms.ModelForm):

    class Meta: 
        model = Categoria
        fields = ('nome', 'tipo')

class accountForm(forms.ModelForm):

    class Meta: 
        model = Lancamento
        fields = ('categoria', 'valor', 'tipo', 'observacao')