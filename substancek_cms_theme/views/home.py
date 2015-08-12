from pyramid.view import view_config

from kotti import DBSession
from kotti.resources import Document


@view_config(context=Document,
             root_only=True,
             renderer='substancek_cms_theme:templates/{0}/index.html')
def home_view(request):
    # you can register a different home page view
    return {}


def includeme(config):
    config.scan(__name__)
