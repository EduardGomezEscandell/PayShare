from source.operation import Operation
from source.agent import Agent
from source.currency import Currency
import unittest

class TestOperation(unittest.TestCase):
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