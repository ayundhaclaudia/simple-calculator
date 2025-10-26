import unittest
from app import app

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_tambah(self):
        response = self.client.get('/calc?a=5&b=3&op=tambah')
        self.assertIn(b'8.0', response.data)

    def test_kurang(self):
        response = self.client.get('/calc?a=5&b=3&op=kurang')
        self.assertIn(b'2.0', response.data)

    def test_kali(self):
        response = self.client.get('/calc?a=2&b=4&op=kali')
        self.assertIn(b'8.0', response.data)

    def test_bagi(self):
        response = self.client.get('/calc?a=8&b=2&op=bagi')
        self.assertIn(b'4.0', response.data)

if __name__ == '__main__':
    unittest.main()
