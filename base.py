from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

def home(request):
    return Response('You are home.')

def hello_world(request):
    return Response('Hello World!')

def unchanged(request):
    return Response("This view doesn't change after override.")

def only_base(request):
    return Response('This view is only in the base configuration.')

def includeme(config):
    config.add_route('home', '/')
    config.add_view(home, route_name='home')
    config.add_route('hello', '/hello')
    config.add_view(hello_world, route_name='hello')
    config.add_route('unchanged', '/unchanged')
    config.add_view(unchanged, route_name='unchanged')


if __name__ == '__main__':
    config = Configurator()
    includeme(config)
    config.add_route('only_base', '/only_base')
    config.add_view(only_base, route_name='only_base')
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()
