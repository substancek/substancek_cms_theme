from kotti.resources import File
from kotti.views.file import attachment_view
from kotti.views.file import inline_view


def includeme(config):    # pragma: no cover
    config.add_view(attachment_view,
                    name='view',
                    context=File,
                    permission='pview')
    config.add_view(inline_view,
                    name='inline-view',
                    context=File,
                    permission='pview')
