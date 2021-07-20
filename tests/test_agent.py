import payshare_testing
from agent import Agent
from currency import Currency
import unittest

class TestAgent(unittest.TestCase):
    def test_construction(self):
        alice = Agent("Alice")
        self.assertEqual(alice.name, "Alice")
        self.assertEqual(len(alice.operations), 0)
        self.assertEqual(len(alice.corrections), 0)
        id = alice.id
        self.assertEqual(alice.id, id)
    
    def test_comparisson(self):
        alice_johnson = Agent("Alice")
        alice_duplicate = alice_johnson
        alice_smith = Agent("Alice")
        bob = Agent("Bob")
        
        self.assertEqual(alice_johnson, alice_johnson)
        self.assertEqual(alice_johnson, alice_duplicate)
        self.assertNotEqual(alice_johnson, bob)
        self.assertNotEqual(alice_johnson, alice_smith)


if __name__ == '__main__':
    unittest.main()