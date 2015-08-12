import pytest
from substancek_cms_theme.views.file import (
    attachment_view,
    inline_view,
    )


class TestFileViews:
    def _create_file(self, config):
        from kotti.resources import File
        self.file = File("file contents", u"myf\xfcle.png", u"image/png")

    def _test_common_headers(self, headers):
        for name in ('Content-Disposition', 'Content-Length', 'Content-Type'):
            assert isinstance(headers[name], str)
        assert headers["Content-Length"] == "13"
        assert headers["Content-Type"] == "image/png"

    @pytest.mark.parametrize("params",
                             [(inline_view, 'inline'),
                              (attachment_view, 'attachment')])
    def test_file_views(self, params, config, filedepot):
        view, disposition = params
        self._create_file(config)
        res = view(self.file, None)

        self._test_common_headers(res.headers)

        assert res.headers["Content-Disposition"] == disposition + \
            ';filename="myfle.png"'

        assert res.app_iter.file.read() == 'file contents'
        res.app_iter.file.seek(0)
        assert res.body == 'file contents'
