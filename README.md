# Simulador de famílias

Esse projeto tem como objetivo gerar e simular a distribuição de famílias para um projeto de seleção de casas do governo.


### Requisitos

Esse projeto foi implementado em python no PyCharm, utilizando o microframework Flask (escolhido por ser bem simples pois o foco é a estrutura do back end) 


# Gerar

É utiliado um número inteiro que será a quantidade de famílias geradas para o teste. Essas famílais são geradas aletoriamente, com nomes, rendas e todos os dados que são necessários para gerar um arquivo .json com os dados de acordo com o que foi proposto.
Esse arquivo .json fica gravado na pasta  "arquivos" do projeto.
Toda vez que se executa o GERAR, esse arquivo é sobrescrivo

# Distribuir
O botão distribuir não utiliza parâmetros. Ele vai acessar a pasta com o arquivo .json, deserelizar o arquivo e fazer o tratamento dado por dado, gerar sua pontuação e colocar na fila de forma ordenada. 
É gravado um arquivo .CSV como saída na pasta "arquivos" dentro do projeto


Eu ainda tenho várias ideias para melhorar a implementação, tanto em relação a código quanto em relação a estrutura, ao cadastro das famílais e até mesmo análise dos pontos*

*um sistema de desempate para pessoas com mesma pontuação, e também algumas avaliações que fiz do CSV através do jupyterNotebook
