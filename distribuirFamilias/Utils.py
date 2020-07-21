from datetime import date, datetime

from distribuirFamilias.Models import Familia, Pessoa, Requisito

from enum import Enum


class TipoRequisito(Enum):
    renda=0
    idade_pretendente=1
    dependentes_menor_idade=2
    status=3



def deserelizar_pessoas(list_pessoas_dict):
    lista_pessoas = []
    for pessoa_dict in list_pessoas_dict:
        id = pessoa_dict['id']
        nome = pessoa_dict['nome']
        tipo = pessoa_dict['tipo']
        data_nascimento = datetime.strptime(pessoa_dict['dataNascimento'], '%d/%m/%Y')

        lista_pessoas.append(Pessoa(id, nome, tipo, data_nascimento))

    return lista_pessoas


def deserelizar_familia(familia_dict):
    id = familia_dict['id']
    pessoas = deserelizar_pessoas(familia_dict['pessoas'])
    rendas = familia_dict['rendas']
    status = familia_dict['status']

    return Familia(id,pessoas,rendas, status)


def get_requisitos():
    lis = []
    requisito = Requisito(TipoRequisito.renda, 0, 900, 5)
    lis.append(requisito)
    requisito = Requisito(TipoRequisito.renda, 901, 1500, 3)
    lis.append(requisito)
    requisito = Requisito(TipoRequisito.renda, 1501, 2000, 1)
    lis.append(requisito)
    requisito = Requisito(TipoRequisito.idade_pretendente, 45, 999, 2)
    lis.append(requisito)
    requisito = Requisito(TipoRequisito.idade_pretendente, 30, 44, 2)
    lis.append(requisito)
    requisito = Requisito(TipoRequisito.idade_pretendente, 0, 30, 1)
    lis.append(requisito)
    requisito = Requisito(TipoRequisito.dependentes_menor_idade, 3, 3, 3)
    lis.append(requisito)
    requisito = Requisito(TipoRequisito.dependentes_menor_idade, 1, 2, 2)
    lis.append(requisito)



    return lis;

def gerar_pontuacao(familia, requisitos):
    gerar_campos_comparacao(familia)

    # gerar pontuação
    for requisito in requisitos:
        if requisito.get_tipo_requisito() not in familia.get_tipos_ocorridos():
            requisito.analisar(familia)


def calcula_pretendentes_menor_idade(pessoas):
    qtdade = 0
    for pessoa in pessoas:
        if(pessoa.get_tipo == 'Dependente' and calcula_idade(pessoa.get_data_nascimento()) <= 18):
            qtdade+=1

    return qtdade




def gerar_campos_comparacao(familia):
    renda = 0
    for rendaPessoa in (familia.rendas):
        renda += rendaPessoa['valor']

    idade_pretendente = calcula_idade(familia.get_data_nascimento_pretendente())

    dependentes_menor_idade = calcula_pretendentes_menor_idade(familia.pessoas)

    dict = {
        TipoRequisito.renda.name:                    renda,
        TipoRequisito.idade_pretendente.name:        idade_pretendente,
        TipoRequisito.dependentes_menor_idade.name   :dependentes_menor_idade
    }
    familia.set_campos_comparacao(dict)

def calcula_idade(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

def get_cabecalho_csv(familia_dict):
    familia = deserelizar_familia(familia_dict)
    gerar_campos_comparacao(familia)

    cabecalho = ['id', 'QtdadeCriterios', 'Pontuacao']
    campos = familia.get_campos_comparacao()
    for item in campos:
        cabecalho.append(item)

    return cabecalho

def gerar_csv(familia):
    return familia.get_sequencia_csv()


