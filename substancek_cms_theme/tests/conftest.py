from pytest import fixture

pytest_plugins = "kotti"

substancek_cms_theme_includes = [
    'kotti',
    'pyramid_html_minifier',
    'kotti.views',
    'substancek_cms_theme',
    'substancek_cms_theme.static',
    'substancek_cms_theme.views.default',
    'substancek_cms_theme.views.image',
    'substancek_cms_theme.views.file',
    'substancek_cms_theme.views.home',
    'substancek_cms_theme.views.document',
    'substancek_cms_theme.views.notfound',
    'substancek_cms_theme.views.forbidden',
]


@fixture(scope='session')
def custom_settings():
    return {
        'kotti.site_title': 'substancek_cms_theme',
        'kotti.use_workflow': 'kotti_backend:workflows/simple_backend.zcml',
        'kotti.asset_overrides': 'substancek_cms_theme:templates/app/kotti-overrides/',
        'pyramid.includes': ' '.join(substancek_cms_theme_includes),
        'kotti.configurators': ' '.join(('substancek_cms_theme.kotti_configure',)),
        }
