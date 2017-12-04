from model.projeto import Projeto

from datetime import datetime

class Mudanca(object):

    def __init__(self, mudanca_id, projeto, descricao, data_solicitacao, aprovada):
        self.mudanca_id = mudanca_id
        self.projeto = projeto
        self.descricao = descricao
        self.data_solicitacao = data_solicitacao
        self.aprovada = aprovada