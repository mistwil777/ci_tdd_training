import unittest
from app.main import add_numbers
    
class TestAddNumbers(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add_numbers(2, 5), 7)

if __name__ == '__main__':
    unittest.main()

    