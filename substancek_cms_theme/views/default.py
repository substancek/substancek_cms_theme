from kotti.interfaces import IContent
from kotti.views.view import view_content_default


def includeme(config):
    config.add_view(view_content_default,
                    context=IContent,
                    )
