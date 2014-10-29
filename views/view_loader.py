from mako.lookup import TemplateLookup

template_lookup = TemplateLookup(
    directories=['templates'],
    module_directory='tmp/mako',
)

asset_base = "feedie:../htdocs/assets"

class ViewLoader(object):

    def __init__(self, request):
        self._request = request

    def load_asset(self, asset_url):
        return self._request.static_url(
            '{0}/{1}'.format(asset_base, asset_url),
           )

    def render_template(self, template_name, **kwargs):
        template = template_lookup.get_template(template_name)
        return template.render(
            load_asset=self.load_asset,
            **kwargs)