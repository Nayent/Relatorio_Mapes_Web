# Relatório Mapes Web

Este repositório tem como objetivo o teste para a fase dois da seleção para vaga de desenvolvedor Django na MAPESolutions.

https://relatorio-mapes.herokuapp.com/

## Algumas funcionalidades:
* Na tela inicial há um campo de pesquisa e abaixo uma lista com todos relatórios

![Alt text](imagesREADME/home.png?raw=true "Home")

* Ao realizar uma busca nos campos, sendo campos não obrigatórios, é encaminhado para uma nova página, porém contendo o mesmo visual da primeira, criando um fluxo de páginas.

![Alt text](imagesREADME/busca.png?raw=true "Home")

* Caso seja buscado um valor inválido será apresentado uma mensagem indicando que não foram encontrado resultados da pesquisa

![Alt text](imagesREADME/nEncontrado.png?raw=true "Home")

* No caso de deixar ambos os campos de pesquisa em branco será retornado todos os valor da lista

### Lembrando que em todos os casos a lista será ordenada em ordem decrescente pela coluna "Gasto por Consulta".
