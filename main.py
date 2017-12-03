import falcon

from controller.teste import ThingsResource

# falcon.API instances are callable WSGI apps
app = falcon.API()

# Teste
app.add_route('/scp/hello', ThingsResource())
