from kotti.interfaces import IFile
from kotti.views.file import attachment_view
from kotti.views.file import inline_view
from kotti.views.file import view


def includeme(config):    # pragma: no cover
    config.add_view(view,
                    name='view',
                    context=IFile,
                    permission='pview')
    config.add_view(inline_view,
                    name='inline-view',
                    context=IFile,
                    permission='pview')
    config.add_view(attachment_view,
                    name='attachment-view',
                    context=IFile,
                    permission='pview')
