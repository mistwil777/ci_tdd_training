#!/usr/bin/env python3

import unittest
import pytest 
from app.main import add_numbers

# def test_add_numbers():
#     assert add_numbers(2, 5) == 7
#     assert add_numbers(2, 2) == 4
#     assert add_numbers(-1, 3) == 2
    
class TestAddNumbers(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add_numbers(2, 5), 7)

    def test_add_same_numbers(self):
        self.assertEqual(add_numbers(2, 2), 4)

    def test_add_negative_and_positive(self):
        self.assertEqual(add_numbers(-1, 3), 2)

if __name__ == '__main__':
    unittest.main()

    