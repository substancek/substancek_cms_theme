class TestTags:

    def test_search_content_for_tag_title(self, root):
        from kotti.resources import Tag, TagsToContents, Content
        from substancek_cms_theme.views.util import search_content_for_tags

        root[u'folder_1'] = Content()
        root[u'folder_1'].tags = [u'first tag', u'second tag']
        root[u'folder_1'][u'content_1'] = Content()
        root[u'folder_1'][u'content_1'].tags = [u'third tag']
        root[u'folder_1'][u'content_2'] = Content()
        root[u'folder_1'][u'content_2'].tags = [u'first tag', u'third tag']

        result = Content.query.join(TagsToContents).join(Tag).filter(
            Tag.title == u'first tag').all()
        assert [res.name for res in result] == [u'folder_1', u'content_2']
        result = Content.query.join(TagsToContents).join(Tag).filter(
            Tag.title == u'second tag').all()
        assert [res.name for res in result] == [u'folder_1']
        result = Content.query.join(TagsToContents).join(Tag).filter(
            Tag.title == u'third tag').all()
        assert [res.name for res in result] == [u'content_1', u'content_2']

        # The same tests again, using content_with_tags():
        #
        #     About expected sort order:
        #
        #         In the first set of tests below, where we search by single
        #         tags, the query in the content_with_tags() function returns
        #         results in hierarchical order, from root.
        #
        # content_with_tags() is written to take a list of tags, but in the
        # default Kotti, presently, after some consideration about specialized
        # add-ons for searching, we do not support multiple tags searching, in
        # part to avoid establishing a specification.
        #
        import mock
        from kotti.testing import DummyRequest
        dummy_request = DummyRequest()
        with mock.patch('substancek_cms_theme.views.util.has_permission') \
                as has_permission:
            has_permission.return_value = True
            result = search_content_for_tags([u'first tag'], dummy_request)
            assert [res['name'] for res in result] == [u'folder_1', u'content_2']
            result = search_content_for_tags([u'second tag'], dummy_request)
            assert [res['name'] for res in result] == [u'folder_1']
            result = search_content_for_tags([u'third tag'], dummy_request)
            assert [res['name'] for res in result] == [u'content_1', u'content_2']

    def test_search_results_for_tag_title(self, root):
        from kotti.resources import Tag, TagsToContents, Content
        from substancek_cms_theme.views.search import search_results_for_tag

        root[u'folder_1'] = Content()
        root[u'folder_1'].tags = [u'first tag', u'second tag']
        root[u'folder_1'][u'content_1'] = Content()
        root[u'folder_1'][u'content_1'].tags = [u'third tag']
        root[u'folder_1'][u'content_2'] = Content()
        root[u'folder_1'][u'content_2'].tags = [u'first tag', u'third tag']

        result = Content.query.join(TagsToContents).join(Tag).filter(
            Tag.title == u'first tag').all()
        assert [res.name for res in result] == [u'folder_1', u'content_2']
        result = Content.query.join(TagsToContents).join(Tag).filter(
            Tag.title == u'second tag').all()
        assert [res.name for res in result] == [u'folder_1']
        result = Content.query.join(TagsToContents).join(Tag).filter(
            Tag.title == u'third tag').all()
        assert [res.name for res in result] == [u'content_1', u'content_2']

        # The same tests again, using content_with_tags():
        #
        #     About expected sort order:
        #
        #         In the first set of tests below, where we search by single
        #         tags, the query in the content_with_tags() function returns
        #         results in hierarchical order, from root.
        #
        # content_with_tags() is written to take a list of tags, but in the
        # default Kotti, presently, after some consideration about specialized
        # add-ons for searching, we do not support multiple tags searching, in
        # part to avoid establishing a specification.
        #
        import mock
        from kotti.testing import DummyRequest
        dummy_request = DummyRequest()
        with mock.patch('substancek_cms_theme.views.util.has_permission') \
                as has_permission:
            has_permission.return_value = True
            dummy_request.GET['tag'] = u'first tag'
            result = search_results_for_tag(None, dummy_request)['results']
            assert [res['name'] for res in result] == [u'folder_1', u'content_2']
            dummy_request.GET['tag'] = u'second tag'
            result = search_results_for_tag(None, dummy_request)['results']
            assert [res['name'] for res in result] == [u'folder_1']
            dummy_request.GET['tag'] = u'third tag'
            result = search_results_for_tag(None, dummy_request)['results']
            assert [res['name'] for res in result] == [u'content_1', u'content_2']
