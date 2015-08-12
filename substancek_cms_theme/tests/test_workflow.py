class TestWorkflow:

    def make_document(self, root):
        from kotti import DBSession
        from kotti.resources import Document

        content = root['document'] = Document()
        DBSession.flush()
        DBSession.refresh(content)
        return content

    def test_workflow_root(self, app, root, workflow):
        from kotti.workflow import get_workflow

        wf = get_workflow(root)
        assert wf.name == u'simple_backend'
        assert root.state == u'public'

    def test_workflow_new_content(self, app, root, workflow, events):
        from kotti.workflow import get_workflow
        from pyramid.security import ALL_PERMISSIONS

        content = self.make_document(root)
        wf = get_workflow(content)
        assert wf.name == u'simple_backend'
        assert content.state == u'private'
        assert content.__acl__[0] == (
            'Allow', 'role:admin', ALL_PERMISSIONS)
        assert content.__acl__[-1] == (
            'Deny', 'system.Everyone', ALL_PERMISSIONS)

        # test public view (pview) and view permissions
        ('Allow', 'system.Everyone', u'pview') not in content.__acl__
        ('Allow', 'system.Everyone', u'view') not in content.__acl__

    def test_workflow_transition(self, app, root, workflow, events):
        from kotti.workflow import get_workflow
        content = self.make_document(root)
        wf = get_workflow(content)
        wf.transition_to_state(content, None, u'public')
        assert content.state == u'public'
        # test public view (pview) and view permissions
        ('Allow', 'system.Everyone', u'pview') in content.__acl__
        ('Allow', 'system.Everyone', u'view') not in content.__acl__
