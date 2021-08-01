from unittest import TestCase


class TestAPI(TestCase):
    def setUp(self):
        from app import create_app
        app = create_app()
        app.testing = True
        self.app = app.test_client()

    def test_get_top_five_posts_success(self):
        req = self.app.get('/posts/top', query_string={
            "url": "https://www.reddit.com",
        })
        self.assertEqual(len(req.json), 5)
        self.assertEqual(req.status_code, 200)

    def test_get_top_five_posts_success_2(self):
        req = self.app.get('/posts/top', query_string={
            "url": "https://www.reddit.com/r/bulgaria",
        })
        self.assertEqual(len(req.json), 5)
        self.assertEqual(req.status_code, 200)

    def test_get_top_five_posts_fail(self):
        req = self.app.get('/posts/top', query_string={
            "url": "http://www.reddit.com",
        })
        self.assertIn('error', req.json)
        self.assertEqual(req.status_code, 400)

    def test_get_top_five_posts_fail_2(self):
        req = self.app.get('/posts/top', query_string={
            "url": "www.reddit.com",
        })
        self.assertIn('error', req.json)
        self.assertEqual(req.status_code, 400)
