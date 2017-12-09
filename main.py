import falcon

from controller.teste import ThingsResource
from controller.pessoa_controller import PessoaController
from controller.pessoa_email_controller import PessoaEmailController

# falcon.API instances are callable WSGI apps
app = falcon.API()

# Teste
app.add_route('/scp/hello', ThingsResource())

# Pessoa
app.add_route('/scp/pessoa', PessoaController())
app.add_route('/scp/pessoa/email/{email}', PessoaEmailController())