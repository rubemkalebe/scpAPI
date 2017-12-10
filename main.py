import falcon

from controller.teste import ThingsResource

from controller.pessoa.pessoa_controller import PessoaController
from controller.pessoa.pessoa_email_controller import PessoaEmailController

from controller.projeto.projeto_controller import ProjetoController
from controller.projeto.projeto_by_ger_controller import ProjetoByGerenteController
from controller.projeto.projeto_by_pat_controller import ProjetoByPatrocinadorController

# falcon.API instances are callable WSGI apps
app = falcon.API()

# Teste
app.add_route('/scp/hello', ThingsResource())

# Pessoa
app.add_route('/scp/pessoa', PessoaController())
app.add_route('/scp/pessoa/email/{email}', PessoaEmailController())

# Projeto
app.add_route('/scp/projeto', ProjetoController())
app.add_route('/scp/projeto/gerente/{gerente_id}', ProjetoByGerenteController())
app.add_route('/scp/projeto/patrocinador/{patrocinador_id}', ProjetoByPatrocinadorController())