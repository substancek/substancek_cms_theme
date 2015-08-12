class TestForbidden:

    def make_document(self, root):
        from kotti import DBSession
        from kotti.resources import Document

        content = root['doc'] = Document(title=u'MyDocument')
        DBSession.flush()
        DBSession.refresh(content)
        return content

    def test_public_document_anonymous(self, root, webtest, db_session):
        doc = self.make_document(root)
        assert doc.state == 'private'

        resp = webtest.get('/doc', headers={'Accept': '*/json'}, status=403)
        # the document is private
        assert resp.status_code == 403
        assert 'substancek_cms_theme' in resp.body
        assert 'MyDocument' not in resp.body

        # the document is public
        from kotti.workflow import get_workflow
        wf = get_workflow(root)
        wf.transition_to_state(doc, None, u'public')
        assert doc.state == u'public'

        resp = webtest.get('/doc', headers={'Accept': '*/json'}, status=200)
        assert resp.status_code == 200
        assert 'substancek_cms_theme' in resp.body
        assert 'MyDocument' in resp.body
