import falcon
import json

from data.entregavelDAO import EntregavelDAO
from model.entregavel import Entregavel

class EntregavelController(object):

    def on_get(self, req, resp, projeto_id):
        entregavelDAO = EntregavelDAO()
        entregaveis = entregavelDAO.retrieve_by_projeto(projeto_id)

        resp.status = falcon.HTTP_200 # ok
        resp.body = json.dumps(entregaveis, default=str)

    def on_post(self, req, resp, projeto_id):
        payload = req.stream.read().decode('utf-8')
        data = json.loads(payload)

        entregavelDAO = EntregavelDAO()
        entregavelDAO.insert(projeto_id, Entregavel(
            None, None, data['nome'], data['descricao'],
            data['data_inicio'], data['data_fim_prev'],
            data['data_fim']
        ))

        resp.status = falcon.HTTP_200 # ok
        resp.body = json.dumps({'msg' : 'Entregavel adicionado'})
