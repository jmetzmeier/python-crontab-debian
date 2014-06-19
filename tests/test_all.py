import glob
import unittest

if __name__ == '__main__':
    test_files = glob.glob('test_*.py')
    modules = [s[:-3] for s in test_files if 'compat' not in s]
    suites = [unittest.defaultTestLoader.loadTestsFromName(s) for s in modules]
    testSuite = unittest.TestSuite(suites)
    text_runner = unittest.TextTestRunner().run(testSuite)
