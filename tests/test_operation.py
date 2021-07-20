import payshare_testing
from operation import Operation
from agent import Agent
from currency import Currency
import unittest

class TestCurrency(unittest.TestCase):
    def test_construction(self):
        alice = Agent("Alice")
        bob = Agent("Bob")
        amount = Currency(2.85)
        descr = "This is a sample description"

        op = Operation(None, alice, [alice, bob], amount, descr)

        self.assertTrue(op.book is None)
        self.assertEqual(op.payer, alice)
        self.assertListEqual(op.consumers, [alice, bob])
        self.assertEqual(op.value, amount)
        self.assertEqual(op.description, descr)


if __name__ == '__main__':
    unittest.main()