from geradorFamilias.Utils import serelizar_lista_pessoas


class Familia:

    def __init__(self, id, pessoas, rendas, status):
        self.id = id
        self.pessoas = pessoas
        self.rendas = rendas
        self.status = status

    def serelizar(self):
        """
        Transforma a classe em dicionário
        :return self:
        """
        pessoas_dict = serelizar_lista_pessoas(self.pessoas),

        return {
            'id': self.id,
            'pessoas': pessoas_dict[0],
            'rendas': self.rendas,
            'status': self.status
        }



class Pessoa:
    def __init__(self, id, nome, tipo, data_nascimento):
        self.id = id
        self.nome = nome
        self.tipo = tipo
        self.data_nascimento = data_nascimento

    def serelizar(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'tipo': self.tipo,
            'dataNascimento': self.data_nascimento.strftime('%d/%m/%Y')
        }
