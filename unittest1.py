import unittest
from fractions import Fraction

"""
https://realpython.com/python-testing/#running-your-tests-from-pycharm
"""


class TestSum (unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(6, result)

    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(1, result)


if __name__ == '__main__':
    unittest.main()
