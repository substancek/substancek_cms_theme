from sqlalchemy import and_
from sqlalchemy import not_
from sqlalchemy import or_

from kotti import DBSession
from kotti.resources import Content
from kotti.resources import Document
from kotti.resources import Tag
from kotti.resources import TagsToContents
from kotti.security import has_permission
from kotti.views.util import content_with_tags


def search_content(search_term, request=None, permission='pview'):

    searchstring = u'%{0}%'.format(search_term)

    # generic_filter can be applied to all Node (and subclassed) objects
    generic_filter = or_(Content.name.like(searchstring),
                         Content.title.like(searchstring),
                         Content.description.like(searchstring))

    results = DBSession.query(Content).filter(generic_filter).\
        order_by(Content.title.asc()).all()

    # specific result contain objects matching additional criteria
    # but must not match the generic criteria (because these objects
    # are already in the generic_results)
    document_results = DBSession.query(Document).filter(
        and_(Document.body.like(searchstring),
             not_(generic_filter)))

    for results_set in [content_with_tags([searchstring]),
                        document_results.all()]:
        [results.append(c) for c in results_set if c not in results]

    result_dicts = []

    for result in results:
        if has_permission(permission, result, request):
            result_dicts.append(dict(
                name=result.name,
                title=result.title,
                description=result.description,
                path=request.resource_path(result)))

    return result_dicts


def search_content_for_tags(tags, request=None, permission='pview'):

    result_dicts = []

    for result in content_with_tags(tags):
        if has_permission(permission, result, request):
            result_dicts.append(dict(
                name=result.name,
                title=result.title,
                description=result.description,
                path=request.resource_path(result)))

    return result_dicts
