class TestHome:

    def test_public_document_anonymous(self, root, webtest, db_session):
        resp = webtest.get('/')
        # the document is private
        assert resp.status_code == 200
        assert 'substancek_cms_theme' in resp.body
