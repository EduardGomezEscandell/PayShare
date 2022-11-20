from payshare.book import Book
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

    def test_correction(self):
        book = Book()
        
        payer = "Alice"
        consumers = ["Joe", "Bob", "Alice"]
        amount = 9.00

        op = book.new_operation(payer, consumers, amount, "Sample operation")

        book.compute_corrections()

        self.assertEqual(book["Alice"].operation_balance(), 6)
        self.assertEqual(book["Joe"].operation_balance(), -3)
        self.assertEqual(book["Bob"].operation_balance(), -3)

        self.assertEqual(book["Alice"].correction_balance(), -6)
        self.assertEqual(book["Joe"].correction_balance(), 3)
        self.assertEqual(book["Bob"].correction_balance(), 3)

        self.assertEqual(book["Alice"].net_balance(), 0)
        self.assertEqual(book["Joe"].net_balance(), 0)
        self.assertEqual(book["Bob"].net_balance(), 0)


if __name__ == '__main__':
    unittest.main()