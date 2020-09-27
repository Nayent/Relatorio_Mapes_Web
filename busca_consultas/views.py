from django.shortcuts import render
from busca_consultas.models import Consulta, Exame, Relatorio

def index(request):

    relatorio = Relatorio.objects.order_by("-gasto_consulta").all()
    consulta = Consulta.objects.order_by("numero_guia").all()
    exame = Exame.objects.order_by("numero_guia_consulta").all()

    valores = []
    qtdes = []
    for i in consulta:
        valor = 0
        qtde = 0
        for j in i.exame_set.all():
            qtde += 1
            valor += j.valor_exame
        valores.append(valor)
        qtdes.append(qtde)

    consultas = {
        "consulta" : consulta,
        "valores" : valores,
        "qtdes" : qtdes
    }

    #Criando lista de nomes ordenadas
    names = []
    for i in consultas["consulta"]:
        names.append(i.nome_medico)
    
    names = sorted(set(names))

    consultas["nomes"] = names

    return render(request, 'index.html', consultas)



def relatorio(request):

    busca_consulta = Consulta.objects.order_by('numero_guia').all()

    consultas = {
        "consulta" : busca_consulta
    }

    #Criando lista de nomes ordenadas
    names = []
    for i in consultas["consulta"]:
        names.append(i.nome_medico)
    
    names = sorted(set(names))

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
