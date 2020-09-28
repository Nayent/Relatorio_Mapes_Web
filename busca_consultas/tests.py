from django.test import TestCase
from .models import Relatorio

class basicTest(TestCase):

    def test_getRelatorio(self):
        relatorio = Relatorio.objects.all()
        for i in relatorio:
            self.assertContains(i.nome_medico)

    def test_getRelatorioFiltered(self):
        searchMedico = "ABEL"
        searchData = "2018-11-16"

        relatorio = Relatorio.objects.filter(nome_medico= searchMedico, data_consulta= searchData)

        for i in relatorio:
            self.assertEqual(i.nome_medico, searchMedico)
            self.assertEqual(i.data_consulta, searchData)