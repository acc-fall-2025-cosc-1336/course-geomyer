#Test decisions from decisions.py
import unittest

from src.homework.c_decisions.decisions import number_to_letter_grade
class Test_Config(unittest.TestCase):
    
        
    def test_get_letter_grade(self):
        self.assertEqual('A', number_to_letter_grade(97))
        self.assertEqual('B', number_to_letter_grade(85))
        self.assertEqual('C', number_to_letter_grade(75))
        self.assertEqual('D', number_to_letter_grade(65))
        self.assertEqual('F', number_to_letter_grade(50))
        