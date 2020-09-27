from django.db import models
from datetime import date


class Consulta(models.Model):
    numero_guia = models.IntegerField(primary_key=True)
    cod_medico = models.IntegerField()
    nome_medico = models.CharField(max_length = 100)
    data_consulta = models.DateField()
    valor_consulta = models.FloatField()
    def __str__(self):
        return str(self.numero_guia)

class Exame(models.Model):
    numero_guia_consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE)
    exame = models.CharField(max_length=100)
    valor_exame = models.FloatField()

class Relatorio(models.Model):
    numero_guia = models.IntegerField()
    nome_medico = models.CharField(max_length = 100)
    data_consulta = models.DateField()
    valor_consulta = models.FloatField()
    gasto_consulta = models.FloatField()
    qtde_exames = models.IntegerField()