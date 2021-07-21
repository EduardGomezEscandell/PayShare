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
        loc["to"]
        loc["from"]

    def test_spanish(self):
        Localization.set("es")
        loc = Localization.get()
        self.assertEqual(loc["no_operation"],"ninguna")
        loc["agent_report"]
        loc["book_report"]
        loc["to"]
        loc["from"]

    def test_catalan(self):
        Localization.set("ca")
        loc = Localization.get()
        self.assertEqual(loc["no_operation"],"res")
        loc["agent_report"]
        loc["book_report"]
        loc["to"]
        loc["from"]

if __name__ == '__main__':
    unittest.main()