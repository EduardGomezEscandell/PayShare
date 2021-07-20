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
    
    def test_eq(self):
        x = Currency(1.08)
        y = Currency(1, 8)
        self.assertEqual(x, y)

    def test_add(self):
        x = Currency(5.30)
        y = Currency(1.0)
        z = x + y
        self.assertEqual(z, 6.30)

    def test_iadd(self):
        x = Currency(2.08)
        x += 5
        self.assertEqual(x, 7.08)
    
    def test_sub(self):
        x = Currency(5.30)
        y = Currency(1.0)
        z = x - y
        self.assertEqual(z, 4.30)

    def test_isub(self):
        x = Currency(2.08)
        x -= 5.0
        self.assertEqual(x, -2.92)

    def test_mul(self):
        x = Currency(5.00)
        z = x * 5
        self.assertEqual(z, 25)

    def test_imul(self):
        x = Currency(2.00)
        x *= 4.0
        self.assertEqual(x, 8)

    def test_div(self):
        x = Currency(5.00)
        z = x / 5
        self.assertEqual(z, 1)

    def test_idiv(self):
        x = Currency(2.00)
        x /= 4.0
        self.assertEqual(x, 0.5)
    
    def test_comparisson(self):
        x = Currency(7.01)
        self.assertLess(x, 7.02)
        self.assertGreater(x, 7.00)
        self.assertGreaterEqual(x, 7.01)

if __name__ == '__main__':
    unittest.main()