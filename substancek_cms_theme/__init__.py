from pyramid.i18n import TranslationStringFactory

_ = TranslationStringFactory('substancek_cms_theme')

from pyramid_html_minifier.config import DEFAULT_PLACEHOLDER

base_includes = [
    'pyramid_html_minifier',
    'substancek_cms_theme',
    'substancek_cms_theme.static',
    'substancek_cms_theme.views.default',
#    'substancek_cms_theme.views.image',
    'substancek_cms_theme.views.file',
    'substancek_cms_theme.views.home',
    'substancek_cms_theme.views.document',
    'substancek_cms_theme.views.notfound',
    'substancek_cms_theme.views.forbidden',
    'substancek_cms_theme.views.search',
]

def kotti_configure(settings):
    assets_configure(settings)

    includes_configure(settings)

def includes_configure(settings):
    settings['pyramid.includes'] += ' {0}'.format(' '.join(base_includes))

def assets_configure(settings):
    placeholder = settings.get(
        'pyramid_html_minifier.placeholder',
        DEFAULT_PLACEHOLDER
        )
    base_asset_overrides = ' substancek_cms_theme:templates/{0}/kotti-overrides/'
    asset_overrides = base_asset_overrides.format(placeholder)
    settings['kotti.asset_overrides'] += asset_overrides

def includeme(config):
    # translations
    config.add_translation_dirs('substancek_cms_theme:locale')
