class Projeto(object):

    def __init__(self, projeto_id, nome, descricao, patrocinador,
                 gerente, equipe, entregaveis, mudancas):
        self.projeto_id = projeto_id
        self.nome = nome
        self.descricao = descricao
        self.patrocinador = patrocinador
        self.gerente = gerente
        self.equipe = equipe
        self.entregaveis = entregaveis
        self.mudancas = mudancas
