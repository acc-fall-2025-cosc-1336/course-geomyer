# Saturday September 6 2025, 2:05:00 PM#
import unittest
import src.homework.b_in_proc_out.main  as b_in_proc_out

class TestBInProcOut(unittest.TestCase):
    def test_multiply_numbers(self):
        self.assertEqual(b_in_proc_out.multiply_numbers(5, 5), 25)
        self.assertEqual(b_in_proc_out.multiply_numbers(7, 7), 49)

    def test_main_function(self):
        # Capture the output of the main function
        import io
        import sys

        captured_output = io.StringIO()          # Create StringIO object
        sys.stdout = captured_output             # Redirect stdout.
        b_in_proc_out.main()                     # Call the main function.
        sys.stdout = sys.__stdout__              # Reset redirect.

        output = captured_output.getvalue()
        self.assertIn("Product of 5 and 5 is: 25", output)
        self.assertIn("Product of 7 and 7 is: 49", output)  
