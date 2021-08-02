from unittest import TestCase


class TestAPI(TestCase):
    def test_url_validator(self):
        from utils import url_validator
        output = url_validator("https://www.reddit.com/r/bulgaria")
        self.assertTrue(output)

    def test_url_validator_2(self):
        from utils import url_validator
        output = url_validator("http://www.reddit.com/r/bulgaria")
        self.assertFalse(output)

    def test_get_reddit_data(self):
        from utils import get_reddit_data
        output = get_reddit_data("http://www.reddit.com/r/bulgaria/.json")
        self.assertIsInstance(output, dict)

    def test_find_top_five_post_titles(self):
        from utils import get_reddit_data, find_top_five_post_titles
        data = get_reddit_data("http://www.reddit.com/r/bulgaria/.json")
        output = find_top_five_post_titles(data)
        self.assertIsInstance(output, list)
        self.assertEqual(len(output), 5)
