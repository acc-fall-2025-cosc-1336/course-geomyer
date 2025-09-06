import unittest
from homework.b_in_proc_out.output import multiply_numbers

class TestMultiplyNumbers(unittest.TestCase):
    """
    Unit tests for the multiply_numbers function.

    Test Cases:
    - test_multiply_seven_by_seven: Verifies that multiplying 7 by 7 returns 49.
    - test_multiply_five_by_five: Verifies that multiplying 5 by 5 returns 25.
    """
    def test_multiply_seven_by_seven(self):
        self.assertEqual(multiply_numbers(7, 7), 49)
    def test_multiply_five_by_five(self):
        self.assertEqual(multiply_numbers(5, 5), 25)
