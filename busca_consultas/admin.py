from django.contrib import admin
from .models import Consulta, Exame

class ListandoConsultas(admin.ModelAdmin):
    list_display = ('numero_guia','nome_medico')

class ListandoExame(admin.ModelAdmin):
    list_display = ('id', 'numero_guia_consulta','exame')

admin.site.register(Consulta, ListandoConsultas)
admin.site.register(Exame, ListandoExame)
