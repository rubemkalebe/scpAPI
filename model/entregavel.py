from model.projeto import Projeto

from datetime import datetime

class Entregavel(object):

    def __init__(self, projeto, entregavel_id, nome, descricao, data_inicio,
                 data_fim_prev, data_fim):
        self.projeto = projeto
        self.entregavel_id = entregavel_id
        self.nome = nome
        self.descricao = descricao
        self.data_inicio = data_inicio
        self.data_fim_prev = data_fim_prev
        self.data_fim = data_fim