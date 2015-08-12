class TestNotFound:

    def test_not_found_view_webtest(self, webtest):
        resp = webtest.get('/doesnotexists', status=404)
        assert resp.status_code == 404
        assert 'substancek_cms_theme' in resp.body

    def test_not_found_view(self):
        from substancek_cms_theme.views.notfound import notfound_view
        from kotti.testing import DummyRequest
        dummy_request = DummyRequest()
        notfound_view(dummy_request)

        assert dummy_request.response.status == '404 Not Found'
