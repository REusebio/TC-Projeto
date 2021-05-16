from django.contrib import admin

# Register your models here.
from .models import Automato, Maquina, Expressao
admin.site.register(Automato)
admin.site.register(Maquina)
admin.site.register(Expressao)
