import unittest
from app import is_even

class TestEvenOdd(unittest.TestCase):

    def test_even(self):
        self.assertTrue(is_even(2))
        self.assertTrue(is_even(10))

    def test_odd(self):
        self.assertFalse(is_even(1))
        self.assertFalse(is_even(5))

if __name__ == "__main__":
    unittest.main()
