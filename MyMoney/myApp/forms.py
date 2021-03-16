from django import forms
from .models import Categoria

class categoryForm(forms.ModelForm):

    class Meta: 
        model = Categoria
        fields = ('nome', 'tipo')