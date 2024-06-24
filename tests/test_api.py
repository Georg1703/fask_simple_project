import unittest
from app import create_app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.client = create_app().test_client()

    def test_personal(self):
        response = self.client.get('/personal')
        self.assertEqual(response.status_code, 200)
        self.assertIn('John Doe', str(response.data))

    def test_experience(self):
        response = self.client.get('/experience')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Company A', str(response.data))

    def test_education(self):
        response = self.client.get('/education')
        self.assertEqual(response.status_code, 200)
        self.assertIn('University X', str(response.data))
