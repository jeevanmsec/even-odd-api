import unittest
from app import app


class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_home_page_loads(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_page_contains_title(self):
        response = self.client.get("/")
        self.assertIn(b"Even or Odd Checker", response.data)


if __name__ == "__main__":
    unittest.main()
