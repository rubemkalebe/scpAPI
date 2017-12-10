import falcon
import json

from data.projetoDAO import ProjetoDAO

class ProjetoByPatrocinadorController(object):

    def on_get(self, req, resp, patrocinador_id):
        projetoDAO = ProjetoDAO()
        projetos = projetoDAO.retrieve_by_patrocinador(patrocinador_id)

        if(projetos != None):
            resp.status = falcon.HTTP_200 # OK!
            resp.body = json.dumps(projetos)
        else:
            resp.status = falcon.HTTP_404 # Not Found
            resp.body = json.dumps({'msg' : 'We could not find projects sponsored by this id'})