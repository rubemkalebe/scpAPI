import falcon
import json

from data.pessoaDAO import PessoaDAO
from model.pessoa import Pessoa

class PessoaController(object):

    def on_get(self, req, resp):
        pessoaDAO = PessoaDAO()
        pessoas = pessoaDAO.fetchall()

        resp.status = falcon.HTTP_200 # OK!
        resp.body = json.dumps(pessoas)

    def on_post(self, req, resp):
        payload = req.stream.read().decode('utf-8')
        data = json.loads(payload)

        pessoaDAO = PessoaDAO()
        pessoaDAO.insert(Pessoa(None, data['nome'], data['departamento'],
                                data['email'], None))

        resp.status = falcon.HTTP_200 # OK!
        resp.body = json.dumps({'msg' : 'Pessoa adicionada: ' + data['nome']})