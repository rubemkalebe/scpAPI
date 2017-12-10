import falcon
import json

from data.pessoaDAO import PessoaDAO
from model.pessoa import Pessoa

class PessoaEmailController(object):

    def on_get(self, req, resp, email):
        pessoaDAO = PessoaDAO()
        p = pessoaDAO.retrieve_by_email(email)

        if(p != None):
            resp.status = falcon.HTTP_200 # OK!
            resp.body = json.dumps(p)
        else:
            resp.status = falcon.HTTP_404 # Not Found
            resp.body = json.dumps({'msg' : 'We could not find a user with this e-mail'})