import unittest

from src.examples.a_example.devprocess import multiply_numbers




suite = unittest.defaultTestLoader.loadTestsFromModule(__import__('src.examples.a_example.devprocess', fromlist=['']))
unittest.TextTestRunner(verbosity=2).run(suite)
