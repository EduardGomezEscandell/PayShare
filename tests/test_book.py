import payshare_testing
from book import Book
import unittest

class TestBook(unittest.TestCase):
    def test_construction(self):
        b = Book()
        self.assertTrue(hasattr(b, "agents"))
        self.assertTrue(hasattr(b, "operations"))
        self.assertTrue(hasattr(b, "corrections"))
    
    def test_new_operation(self):
        book = Book()
        
        alice = book["Alice"]
        
        payer = "Alice"
        consumers = ["Joe", "Bob"]

        op = book.new_operation(payer, consumers, 13.05, "Sample operation")

        self.assertEqual(len(book.operations), 1)
        self.assertEqual(book.operations[0], op)
        self.assertEqual(book.operations[0].payer.name, "Alice")
        self.assertEqual(book.operations[0].payer, alice)
        self.assertEqual(len(book.agents), 3) # Alice, Joe and Bob
        self.assertEqual(len(alice.operations), 1)


if __name__ == '__main__':
    unittest.main()