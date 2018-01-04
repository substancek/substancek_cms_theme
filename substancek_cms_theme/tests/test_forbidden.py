class TestForbidden:

    def test_forbidden_view_webtest(self, root, webtest, db_session):
        from kotti.resources import Document
        root[u'doc'] = doc = Document(title=u'document')
        db_session.flush()
        assert doc.state == 'private'

        resp = webtest.get('/doc', headers={'Accept': '*/json'}, status=403)
        assert resp.status_code == 403
        assert 'substancek_cms_theme' in resp.body

    def test_forbidden_view(self):
        from substancek_cms_theme.views.forbidden import forbidden_view
        from kotti.testing import DummyRequest
        dummy_request = DummyRequest()
        forbidden_view(dummy_request)

        assert dummy_request.response.status == '403 Forbidden'
