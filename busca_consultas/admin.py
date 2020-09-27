from django.contrib import admin
from .models import Consulta, Exame, Relatorio

class ListandoConsultas(admin.ModelAdmin):
    list_display = ('numero_guia','nome_medico')

class ListandoExame(admin.ModelAdmin):
    list_display = ('id', 'numero_guia_consulta','exame')

class ListandoRelatorio(admin.ModelAdmin):
    list_display = ('nome_medico')

admin.site.register(Consulta, ListandoConsultas)
admin.site.register(Exame, ListandoExame)
admin.site.register(Relatorio, ListandoRelatorio)
