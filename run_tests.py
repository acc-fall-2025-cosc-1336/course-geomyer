import unittest 

from src.homework.b_in_proc_out import output


suite = unittest.defaultTestLoader.loadTestsFromModule('src.homework.b_in_proc_out.main')    

unittest.TextTestRunner(verbosity=2).run(suite)
