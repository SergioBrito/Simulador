import csv
import json

from distribuirFamilias import Utils
from distribuirFamilias.Models import Familia, Fila
from distribuirFamilias.Utils import deserelizar_familia, get_requisitos, gerar_pontuacao, get_cabecalho_csv, gerar_csv


def distribuir_familias(dados):

    fila = Fila(get_requisitos())
    fila.gerar_metadados_iniciais()

    for familia_dict in(dados):
        familia = deserelizar_familia(familia_dict)
        gerar_pontuacao(familia,fila.get_requisitos())

        sequencia = gerar_csv(familia)
        print(sequencia)
        fila.add_sequencia_csv_familia(familia.get_pontuacao() ,sequencia)

    return fila.get_fila_csv()




def main():
    with open('../arquivos/meu_arquivo.json', 'r') as json_file:
        dados = json.load(json_file)

    distribuir_familias(dados)


if __name__ == "__main__":
    main()