from kotti.views.view import search_results
from .util import search_content_for_tags


def search_results_for_tag(context, request):
    results = []
    if u'tag' in request.GET:
        # Single tag searching only, is allowed in default Kotti. Add-ons can
        # utilize search_content_for_tags(tags) to enable multiple tags
        # searching, but here it is called with a single tag.
        tags = [request.GET[u'tag'].strip()]
        results = search_content_for_tags(tags, request)
    return {'results': results}


def includeme(config):    # pragma: no cover
    config.add_view(
        search_results,
        name='search-results',
        renderer='substancek_cms_theme:templates/{0}/search-results.html',
        )
    config.add_view(
        search_results_for_tag,
        name='search-tag',
        renderer='substancek_cms_theme:templates/{0}/search-results.html',
        )
