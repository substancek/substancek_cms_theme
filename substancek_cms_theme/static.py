from pyramid_html_minifier.config import DEFAULT_PLACEHOLDER

def includeme(config):   # pragma: no cover
    settings = config.registry.settings
    placeholder = settings.get('pyramid_html_minifier.placeholder', DEFAULT_PLACEHOLDER)

    # styles
    default_styles_path = 'substancek_cms_theme:templates/{0}/styles/'.format(DEFAULT_PLACEHOLDER)
    config.add_static_view('styles',
                           default_styles_path)
    if placeholder == DEFAULT_PLACEHOLDER:
        config.override_asset(to_override=default_styles_path,
                              override_with='substancek_cms_theme:templates/.tmp/styles/')
    else:
        styles_path = 'substancek_cms_theme:templates/{0}/styles/'.format(placeholder)
        config.override_asset(to_override=default_styles_path,
                              override_with=styles_path)

    # bower_components
    if placeholder == DEFAULT_PLACEHOLDER:
        # assume not production
        config.add_static_view('bower_components',
                               'substancek_cms_theme:templates/bower_components/')

    # scripts
    default_scripts_path = 'substancek_cms_theme:templates/{0}/scripts/'.format(DEFAULT_PLACEHOLDER)
    config.add_static_view('scripts',
                           default_scripts_path)
    if placeholder != DEFAULT_PLACEHOLDER:
        # assume not production
        scripts_path = 'substancek_cms_theme:templates/{0}/scripts/'.format(placeholder)
        config.override_asset(to_override=default_scripts_path,
                              override_with=scripts_path)

    # fonts
    default_fonts_path = 'substancek_cms_theme:templates/{0}/fonts/'.format(DEFAULT_PLACEHOLDER)
    config.add_static_view('fonts',
                           default_fonts_path)
    if placeholder == DEFAULT_PLACEHOLDER:
        config.override_asset(to_override=default_fonts_path,
                              override_with='substancek_cms_theme:templates/.tmp/fonts/')
    else:
        fonts_path = 'substancek_cms_theme:templates/{0}/fonts/'.format(placeholder)
        config.override_asset(to_override=default_fonts_path,
                              override_with=fonts_path)

    # substancek_cms_theme's master template
    if placeholder != DEFAULT_PLACEHOLDER:
        base_index = 'substancek_cms_theme:templates/{0}/index.html'
        index_default = base_index.format(DEFAULT_PLACEHOLDER)
        index_override = base_index.format(placeholder)
        config.override_asset(to_override=index_default,
                              override_with=index_override)
