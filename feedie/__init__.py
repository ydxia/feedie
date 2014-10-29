import views

from config.routes import set_routes
from pyramid.config import Configurator
from views.view_loader import asset_base

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('tzf.pyramid_yml')
    config.add_static_view('assets', asset_base, cache_max_age=3600)
    set_routes(config)
    config.scan(views)
    return config.make_wsgi_app()
