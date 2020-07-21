class Familia:
    def __init__(self, id, pessoas, rendas, status):
        self.id = id
        self.pessoas = pessoas
        self.rendas = rendas
        self.status = status
        self.campos_comparacao = []
        self.tipo_pontuacao = {}
        self.pontuacao = 0
        self.tipos_ocorridos = []


    def get_data_nascimento_pretendente(self):
        return self.pessoas[0].get_data_nascimento()

    def set_campos_comparacao(self, campos_comparacao):
        self.campos_comparacao = campos_comparacao

    def get_campos_comparacao(self):
        return self.campos_comparacao

    def add_tipo_pontuacao(self, tipo, pontuacao):
        self.tipo_pontuacao = {tipo.name: pontuacao}
        self.pontuacao += pontuacao
        self.tipos_ocorridos.append(tipo)

    def get_tipos_ocorridos(self):
        return self.tipos_ocorridos

    def get_pontuacao(self):
        return self.pontuacao

    def get_sequencia_csv(self):
        list = [self.id, len(self.tipos_ocorridos), self.pontuacao]
        campos = self.get_campos_comparacao()
        asas =self.campos_comparacao

        for item in self.campos_comparacao:
            list.append(self.campos_comparacao[item])

        return list


class Pessoa:
    def __init__(self, id, nome, tipo, data_nascimento):
        self.id = id
        self.nome = nome
        self.tipo = tipo
        self.data_nascimento = data_nascimento

    def get_data_nascimento(self):
        return self.data_nascimento

    def get_tipo(self):
        return self.tipo


class Requisito:
    def __init__(self, tipo_requisito, valor_inicial, valor_final, pontuacao):
        self.tipo_requisito = tipo_requisito
        self.valor_inicial = valor_inicial
        self.valor_final = valor_final
        self.pontuacao = pontuacao

    def analisar(self, familia):
        campos = familia.get_campos_comparacao()
        valor = campos[self.tipo_requisito.name]
        if self.valor_inicial <= valor <= self.valor_final:
            familia.add_tipo_pontuacao(self.tipo_requisito, self.pontuacao)

    def get_tipo_requisito(self):
        return self.tipo_requisito

class Fila:
    def __init__(self, requisitos):
        self.lista_familias = []
        self.metadados = []
        self.requisitos = requisitos
        self.pontos_max = 11
        self.fila_csv = []

    def gerar_metadados_iniciais(self):
        for i in range(self.pontos_max):
            self.metadados.append(0)

    def add_familia_na_lista(self, familia):
        posicao = self.metadados[familia.get_pontuacao()]
        self.lista_familias.insert(posicao, familia)
        self.organizar_metadados_apos_insercao(posicao)

    def organizar_metadados_apos_insercao(self, posicao):
        for i in range (posicao):
            self.metadados[i] = self.metadados[i] + 1

    def get_requisitos(self):
        return self.requisitos

    def get_posicao_por_ponto(self, pontuacao):
        return self.metadados[pontuacao]

    def add_sequencia_csv_familia(self, pontuacao, sequencia):
        posicao =self.get_posicao_por_ponto(pontuacao)
        self.fila_csv.insert(posicao, sequencia)
        self.organizar_metadados_apos_insercao(pontuacao)

    def get_fila_csv(self):
        return self.fila_csv











