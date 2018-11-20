import unittest
from main import web


class FirstTest(unittest.TestCase):
    def setUp(self):
        self.app = web.app.test_client()

    def test_homepage(self):
        req = self.app.get('/')
        self.assertEqual(req.status, '200 OK')
        self.assertIn('HyenaCORP Project', str(req.data))

    def test_post_good_word(self):
        data = {
            'example': 'nice'
        }
        req = self.app.post('/', data=data)
        self.assertEqual(req.status, '200 OK')
        self.assertIn(f'Results for: {data["example"]}', str(req.data))

    def test_post_bad_word(self):
        data = {
            'example': 'cock'
        }
        req = self.app.post('/', data=data)
        self.assertEqual(req.status, '200 OK')
        self.assertIn('Input should not be a profanity', str(req.data))

    def test_post_space_query(self):
        data = {
            'example': ' '
        }
        req = self.app.post('/', data=data)
        self.assertEqual(req.status, '200 OK')
        self.assertIn('Input can contain only letters', str(req.data))