import payshare_testing
from agent import Agent
from operation import Operation
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
    
    def test_balance(self):
        bob = Agent("Bob")
        alice = Agent("Alice")
        
        self.assertEqual(bob.operation_balance(), 0)
        
        op1 = Operation(None, bob, [alice], 10.0, "Test transaction")
        bob.append_operation(op1)
        alice.append_operation(op1)

        self.assertEqual(bob.operation_balance(), 10)
                
        op2 = Operation(None, alice, [bob], 5.0, "Test transaction #2")
        bob.append_operation(op2)
        alice.append_operation(op1)

        self.assertEqual(bob.operation_balance(), 5)

if __name__ == '__main__':
    unittest.main()