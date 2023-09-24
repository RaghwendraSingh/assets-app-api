"""
Sample Tests
"""

from django.test import SimpleTestCase

from app import calc


class CalcTest(SimpleTestCase):
    """
    Test Cases for calculator
    """
    def test_add_numers(self):
        """Test case for add function of module calc"""
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """
        Test case for subtracting 2 numbers of module calc
        """
        res = calc.subtract(10, 15)

        self.assertEqual(res, 5)
