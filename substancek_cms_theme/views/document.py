from pyramid.view import view_config
from kotti.resources import Document


@view_config(context=Document,
             renderer='substancek_cms_theme:templates/{0}/document.html',
             name='view',
             permission='pview')
def document_view(request):
    return {}


def includeme(config):   # pragma: no cover
    config.scan(__name__)
