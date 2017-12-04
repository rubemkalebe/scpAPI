from model.projeto import Projeto

class Pessoa(object):

    def __init__(self, pessoa_id, nome, departamento, email, projetos):
        self.pessoa_id = pessoa_id
        self.nome = nome
        self.departamento = departamento
        self.email = email
        self.projetos = projetos