import unittest


from test_agent import TestAgent
from test_book import TestBook
from test_currency import TestCurrency
from test_log_reader import TestLogReader
from test_operation import TestOperation

def AssembleTestSuite():
    suite = unittest.TestSuite()

    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestAgent))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestBook))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestCurrency))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestLogReader))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestOperation))

    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(AssembleTestSuite())