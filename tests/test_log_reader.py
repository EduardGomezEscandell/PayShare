import payshare_testing
from book import Book
from log_reader import LogReader
import unittest
import os

class WorkFolderScope:
    def __init__(self, work_folder):
        self.currentPath = os.getcwd()
        self.scope = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)),work_folder))

    def __enter__(self):
        os.chdir(self.scope)

    def __exit__(self, type, value, traceback):
        os.chdir(self.currentPath)


class TestLogReader(unittest.TestCase):
    def test_log_reader(self):
        book = Book()

        with WorkFolderScope("data"):
            reader = LogReader(book, "sample.tsb")
            reader.open()
            
            while reader.next():
                pass
            
            reader.close()

        self.assertEqual(len(book.agents), 5)

if __name__ == '__main__':
    unittest.main()