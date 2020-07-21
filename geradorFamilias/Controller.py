from random import randint
import json

from geradorFamilias.Models import Familia, Pessoa
from geradorFamilias.Utils import gerar_data_nascimento, gerar_nome_aleatorio


def gerar_pessoas_familia(pessoas_geral):
    """
    Esse método gera:
    Pretendente: 1
    Cônjuge: 1
    Dependentes: entre 0 e 4

    :param pessoasGeral: (serve para controlar o ID das pessoas)
    :return:

    """
    pessoas=[]

    #Pretendente
    pessoa = Pessoa(len(pessoas_geral), gerar_nome_aleatorio(), "Pretendente",gerar_data_nascimento("Pretendente") )
    pessoas.append(pessoa)
    pessoas_geral.append(pessoa)

    #Cônjuge
    pessoa = Pessoa(len(pessoas_geral), gerar_nome_aleatorio(), "Conjuge", gerar_data_nascimento("Conjuge"))
    pessoas.append(pessoa)
    pessoas_geral.append(pessoa)

    #dependentes
    dependentes = randint(0,4)
    for i in range(dependentes):
        pessoa = Pessoa(len(pessoas_geral), gerar_nome_aleatorio() + str(i+1), "Dependente", gerar_data_nascimento("Dependente"))
        pessoas.append(pessoa)
        pessoas_geral.append(pessoa)

    return pessoas


def gerar_rendas(pessoas):
    """
    Gera rendas para Pretendente e Conjuge
    :param pessoas:
    :return rendas:
    """
    rendas = []

    for pessoa in pessoas:
        if pessoa.tipo == 'Pretendente':
            rendas.append({'pessoaId': pessoa.id, 'valor': randint(300, 5000)})

        if pessoa.tipo =='Conjuge':
            rendas.append({'pessoaId': pessoa.id, 'valor': randint(0, 2000)})

    return rendas


def gerar_familias(qtdade_familias: object) -> object:


    """
    Esse método gera a quantidade de famílias selecionadas de forma randômica
    para testar a funcionalidade de distribuir famílias.

    :param qtdadeFamilias:
    :return:
    """

    pessoasGeral = []
    familias_geral = []

    for i in range(qtdade_familias):
        pessoas = gerar_pessoas_familia(pessoasGeral)

        rendas = gerar_rendas(pessoas)
    
        status = '1'
        
        familia = Familia(i, pessoas, rendas, status)

        familias_geral.append(familia.serelizar())

    return familias_geral


