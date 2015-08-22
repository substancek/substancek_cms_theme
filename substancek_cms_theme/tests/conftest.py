from pytest import fixture

pytest_plugins = "kotti"


@fixture(scope='session')
def custom_settings():
    return {
        'kotti.site_title': 'substancek_cms_theme',
        'kotti.use_workflow': 'kotti_backend:workflows/simple_backend.zcml',
        'kotti.asset_overrides': 'substancek_cms_theme:templates/app/kotti-overrides/',
        'kotti.base_includes': ' kotti kotti.views',
        'kotti.configurators': ' '.join(('substancek_cms_theme.kotti_configure',)),
        'kotti.search_content': 'substancek_cms_theme.views.util.search_content',
        }
