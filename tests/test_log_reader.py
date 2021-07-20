import payshare_testing
from book import Book
from log_reader import LogReader
import unittest

class TestLogReader(unittest.TestCase):
    def test_log_reader(self):
        book = Book()

        with payshare_testing.WorkFolderScope("data"):
            reader = LogReader(book, "sample.tsb")
            reader.open()
            
            while reader.next():
                pass
            
            reader.close()

        self.assertEqual(len(book.agents), 5)

if __name__ == '__main__':
    unittest.main()