import unittest 

from src.homework.b_in_proc_out.output import multiply_numbers

suite = unittest.defaultTestLoader.loadTestsFromModule(multiply_numbers)
unittest.TextTestRunner(verbosity=2).run(suite)
