import payshare_testing
from agent import Agent
from operation import Operation
from book import Book
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

    def test_report(self):
        book = Book()
        
        book.new_operation("Alice", ["Joe", "Bob", "Alice"], 25, "Alice buys a round for the group")
        book.new_operation("Bob", ["Joe", "Bob", "Alice"], 5, "Bob pays for the tip")

        book.compute_corrections()

        expected_text = ""                                     \
        "Report for Joe\n"                                     \
        "\n"                                                   \
        "You have payed for the following operations:\n"       \
        "  (nothing)\n"                                        \
        "You have benefited from the following operations:\n"  \
        "      8.33 EUR : Alice buys a round for the group\n"  \
        "      1.66 EUR : Bob pays for the tip\n"              \
        "This results in a balance of -10.00 EUR\n"            \
        "\n"                                                   \
        "In order to set the balance to zero you will pay:\n"  \
        "     10.00 EUR to Alice\n"                            \
        "and you will receive:\n"                              \
        "  (nothing)\n"


        self.assertEqual(book["Joe"].report(), expected_text)

if __name__ == '__main__':
    unittest.main()