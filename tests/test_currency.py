import payshare_testing
from source.currency import Currency
import unittest

class TestCurrency(unittest.TestCase):
    def test_construction_empty(self):
        x = Currency()
        self.assertEqual(x.value, 0)


    def test_construction_int(self):
        x = Currency(3, 5)
        self.assertEqual(x.value, 305)


    def test_construction_copy(self):
        x = Currency(1.23)
        self.assertEqual(x.value, 123)

        y = Currency(x)
        self.assertEqual(y.value, 123)


if __name__ == '__main__':
    unittest.main()