# -*- coding: utf-8 -*-
import pytest
from substancek_cms_theme.views.file import (
    attachment_view,
    inline_view,
    )
from kotti.testing import asset


class TestFileViews:

    def _create_file(self, config):
        from kotti.resources import File
        self.file = File(asset('logo.png').read(), u"myfüle.png", u"image/png")

    def _test_common_headers(self, headers):
        for name in ('Content-Disposition', 'Content-Length', 'Content-Type'):
            assert isinstance(headers[name], str)
        assert headers["Content-Length"] == "55715"
        assert headers["Content-Type"] == "image/png"

    @pytest.mark.parametrize("params",
                             [(inline_view, 'inline'),
                              (attachment_view, 'attachment')])
    def test_file_views(self, params, config, filedepot, dummy_request,
                        depot_tween):
        view, disposition = params
        self._create_file(config)

        res = view(self.file, dummy_request)

        self._test_common_headers(res.headers)

        assert res.content_disposition.startswith(
            '{0}; filename=my'.format(disposition))

        assert res.app_iter.file.read() == asset('logo.png').read()
        res.app_iter.file.seek(0)
        assert res.body == asset('logo.png').read()
