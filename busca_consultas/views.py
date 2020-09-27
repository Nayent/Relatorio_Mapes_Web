from django.shortcuts import render
from busca_consultas.models import Consulta, Exame

def index(request):

    consulta = Consulta.objects.order_by("numero_guia").all()

    consultas = {
        "consulta" : consulta
    }

    names = []
    for i in consultas["consulta"]:
        names.append(i.nome_medico)
    
    names = sorted(set(names))

    consultas["nomes"] = names

    exame = Exame.objects.order_by("numero_guia_consulta").all()

    return render(request, 'index.html', consultas)

def relatorio(request):

    busca_consulta = Consulta.objects.order_by('numero_guia').all()

    consultas = {
        "consulta" : busca_consulta
    }

    names = []
    for i in consultas["consulta"]:
        names.append(i.nome_medico)
    
    names = sorted(set(names))

    if "nomeMedico" in request.GET:
        nome_busca = request.GET['nomeMedico']
        date_busca = request.GET['date']

        if nome_busca == "Nenhuma opção" and date_busca != "":
            date_busca = date_busca.split('/')

            date_busca1 = []
            for i in range(len(date_busca) - 1 , - 1 , - 1 ):
                date_busca1.append(date_busca[i])

            date_busca = ("-").join(date_busca1)
            if relatorio:
                busca_consulta = busca_consulta.filter(data_consulta = date_busca)

        if nome_busca != "Nenhuma opção" and date_busca == "":
            if relatorio:
                busca_consulta = busca_consulta.filter(nome_medico__icontains = nome_busca)

        if nome_busca != "Nenhuma opção" and date_busca != "":
            date_busca = date_busca.split('/')

            date_busca1 = []
            for i in range(len(date_busca) - 1 , - 1 , - 1 ):
                date_busca1.append(date_busca[i])

            date_busca = ("-").join(date_busca1)

            if relatorio:
                busca_consulta = busca_consulta.filter(nome_medico__icontains = nome_busca, data_consulta = date_busca)
                
    dados = {
        "consulta" : busca_consulta,
        "nomes" : names
    }


    return render(request, "relatorio.html", dados)
