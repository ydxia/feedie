from pyramid.response import Response
from pyramid.view import view_config

from views.view_loader import ViewLoader


@view_config(route_name='home')
class HomeView(ViewLoader):

    def __init__(self, request):
        super(HomeView, self).__init__(request)
    
    def __call__(self):
        body = self.render_template('feed.mako')
        response = Response(body)
        return response