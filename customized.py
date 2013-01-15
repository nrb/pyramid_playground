from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

def new_hello(request):
    return Response('this is the new hello world!')

def new_home(request):
    return Response('This is home now.')

if __name__ == '__main__':
    config = Configurator()
    config.include('base') # automatically includes 'base.includeme'
    config.add_view(new_hello, route_name='hello')
    config.add_view(new_home, route_name='home')
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()
