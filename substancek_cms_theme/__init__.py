from pyramid.i18n import TranslationStringFactory

_ = TranslationStringFactory('substancek_cms_theme')

from pyramid_html_minifier.config import DEFAULT_PLACEHOLDER


def kotti_configure(settings):
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
