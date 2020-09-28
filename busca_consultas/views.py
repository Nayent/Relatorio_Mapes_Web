from django.shortcuts import render
from busca_consultas.models import Consulta, Exame, Relatorio


def listaNomes(consultas):
    names = []
    for i in consultas:
        names.append(i.nome_medico)
    
    names = sorted(set(names))
    return names

def getRelatorio():
    relatorio = Relatorio.objects.order_by("-gasto_consulta").all()
    return relatorio

def index(request):

    relatorio = getRelatorio()

    consultas = {
        "consulta" : relatorio,
    }

    names = listaNomes(consultas["consulta"])

    consultas["nomes"] = names

    return render(request, 'index.html', consultas)



def relatorio(request):

    busca_consulta = getRelatorio()

    consultas = {
        "consulta" : busca_consulta
    }

    names = listaNomes(consultas["consulta"])

    #Alternativas de pesquisa
    #Caso não seja preenchido nem nome nem data será mostrado todos os dados
    if "nomeMedico" in request.GET:
        nome_busca = request.GET['nomeMedico']
        date_busca = request.GET['date']

        #Apenas data
        if nome_busca == "Nenhuma opção" and date_busca != "":
            date_busca = date_busca.split('/')

            date_busca1 = []
            for i in range(len(date_busca) - 1 , - 1 , - 1 ):
                date_busca1.append(date_busca[i])

            date_busca = ("-").join(date_busca1)
            if relatorio:
                busca_consulta = busca_consulta.filter(data_consulta = date_busca)

        #Apenas nome
        if nome_busca != "Nenhuma opção" and date_busca == "":
            if relatorio:
                busca_consulta = busca_consulta.filter(nome_medico__icontains = nome_busca)

        #Nome & data
        if nome_busca != "Nenhuma opção" and date_busca != "":
            date_busca = date_busca.split('/')

            #Transformando DD/MM/YYYY em YYYY-MM-DD
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
