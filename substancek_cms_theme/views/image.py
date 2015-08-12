from pyramid.view import view_config

from kotti.interfaces import IImage
from kotti.views.image import ImageView


@view_config(context=IImage,
             name='image',
             permission='pview')
def image_view(request, subpath=None):
    view_instance = ImageView(request.context, request)
    return view_instance.image(subpath=subpath)


@view_config(context=IImage,
             name='view',
             permission='pview')
def image_default_view(request):
    view_instance = ImageView(request.context, request)
    return view_instance.image()


def includeme(config):    # pragma: no cover
    config.scan(__name__)
