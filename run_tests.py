import unittest 

from src.homework.a_dev_process import dev_process


suite = unittest.defaultTestLoader.loadTestsFromModule(__import__('src.examples.a_example.devprocess', fromlist=['']))
unittest.TextTestRunner(verbosity=2).run(suite)
