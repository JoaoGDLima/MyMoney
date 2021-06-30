from django.contrib import admin

from .models import Categoria
from .models import Lancamento
from .models import Teste

admin.site.register(Categoria)
admin.site.register(Lancamento)
admin.site.register(Teste)