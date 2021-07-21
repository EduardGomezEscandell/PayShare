import payshare_testing
from localization import Localization
import unittest

class TestLocalization(unittest.TestCase):
    def test_default(self):
        Localization.global_localization = None
        loc = Localization.get()
        self.assertEqual(loc["no_operation"],"nothing")
        loc["agent_report"]
        loc["book_report"]

    def test_spanish(self):
        Localization.set("es")
        loc = Localization.get()
        self.assertEqual(loc["no_operation"],"ninguna")
        loc["agent_report"]
        loc["book_report"]

    def test_catalan(self):
        Localization.set("ca")
        loc = Localization.get()
        self.assertEqual(loc["no_operation"],"cap")
        loc["agent_report"]
        loc["book_report"]

if __name__ == '__main__':
    unittest.main()