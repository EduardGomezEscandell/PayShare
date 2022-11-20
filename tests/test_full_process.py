import payshare_testing
from payshare.book import Book
from payshare.log_reader import LogReader
from payshare.agent import Agent
from payshare.operation import Operation
import unittest

class TestFullProcess(unittest.TestCase):
    def setUp(self):
        """
        Operations and agents are sorted by their ID.
        To ensure the output is always the same, prior information must be removed.
        """
        Agent.reset_id_counter()
        Operation.reset_id_counter()
    
    def test_full_process(self):
        
        with payshare_testing.WorkFolderScope("data"):
            book = Book()
            reader = LogReader(book, "long_sample.tsb")
            book.load_from_file(reader)
            book.compute_corrections()

            report = ""
            for agent in book.agents.values():
                report += "-------------------------------------\n"
                report += agent.report()
            
            report += "\n-------------- SUMMARY --------------\n"
            report += book.report()

            with open("expected_output.txt", "r") as f:
                expected_output = f.read()
            
            self.assertEqual(report, expected_output)

if __name__ == '__main__':
    unittest.main()