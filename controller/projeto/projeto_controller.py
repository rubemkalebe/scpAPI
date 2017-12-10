import falcon
import json

from data.projetoDAO import ProjetoDAO
from model.projeto import Projeto
from model.pessoa import Pessoa

class ProjetoController(object):

    def on_get(self, req, resp):
        projetoDAO = ProjetoDAO()
        projetos = projetoDAO.fetchall()

        resp.status = falcon.HTTP_200 # OK!
        resp.body = json.dumps(projetos)

    def on_post(self, req, resp):
        payload = req.stream.read().decode('utf-8')
        data = json.loads(payload)

        projetoDAO = ProjetoDAO()
        projetoDAO.insert(Projeto(None, data['nome'], data['descricao'],
                                Pessoa(data['idPatrocinador'], None, None, None, None),
                                Pessoa(data['idGerente'], None, None, None, None),
                                data['equipe'], None, None))

        resp.status = falcon.HTTP_200 # OK!
        resp.body = json.dumps({'msg' : 'Projeto adicionado: ' + data['nome']})