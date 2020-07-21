import csv
import time
from flask import Flask, render_template, request
import json

from distribuirFamilias import Controller as distContr
from distribuirFamilias.Controller import distribuir_familias
from distribuirFamilias.Models import Fila
from distribuirFamilias.Utils import get_cabecalho_csv, get_requisitos
from geradorFamilias import Controller as gerarContr

app =Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/gerar")
def gerar():
    return render_template('gerar.html')

@app.route("/distribuir")
def distribuir():
    return render_template('distribuir.html')



@app.route('/gerar_familias', methods = ['POST'])
def gerar_familias():

    inicio = time.time()

    qtdade_familias = request.form['quantidade-familias']
    quantidade_familias = int(qtdade_familias)

    if quantidade_familias > 0:
        familias = gerarContr.gerar_familias(quantidade_familias)

        with open('arquivos/meu_arquivo.json', 'w') as f:
            json.dump(familias, f, indent=4)

    fim = time.time()
    tempo_execucao = fim - inicio

    return render_template('gerar.html', quantidade_familia = quantidade_familias, tempo_execucao="%.2f" % round(tempo_execucao,2))

@app.route('/distribuir_familias', methods = ['POST'])
def distribuir_familias():


    inicio = time.time()



    fila = Fila(get_requisitos())
    fila.gerar_metadados_iniciais()

    with open('arquivos/meu_arquivo.json', 'r') as json_file:
        dados = json.load(json_file)

    sequencias_csv = distContr.distribuir_familias(dados)

    with open('arquivos/familias.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(get_cabecalho_csv(dados[0]))
        writer.writerows(sequencias_csv)

    fim = time.time()
    tempo_execucao = fim - inicio

    return render_template('distribuir.html', distribuido=True, tempo_execucao="%.2f" % round(tempo_execucao,2))


if(__name__ == '__main__'):
    app.run()
d