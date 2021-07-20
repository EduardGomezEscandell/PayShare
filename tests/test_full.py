import payshare_testing
from book import Book
from log_reader import LogReader
import unittest

class TestOperation(unittest.TestCase):
    def test_full_process(self):
        
        with payshare_testing.WorkFolderScope("data"):
            book = Book()
            reader = LogReader(book, "long_sample.tsb")
            book.load_from_file(reader)
            book.compute_corrections()

            for agent in book.agents.values():
                print("------------------------")
                print(agent.report())


if __name__ == '__main__':
    unittest.main()