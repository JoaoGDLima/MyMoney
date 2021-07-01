from django.contrib import admin

from .models import Categoria
from .models import Lancamento

admin.site.register(Categoria)
admin.site.register(Lancamento)
admin.site.register(Tipo2)