from source.localization import Localization
import unittest

class TestLocalization(unittest.TestCase):
    def test_default(self):
        loc = Localization()
        self.assertEqual(loc["no_operation"],"nothing")
        loc["agent_report"]
        loc["book_report"]
        loc["to"]
        loc["from"]

    def test_spanish(self):
        loc = Localization("es")
        self.assertEqual(loc["no_operation"],"ninguna")
        loc["agent_report"]
        loc["book_report"]
        loc["to"]
        loc["from"]

    def test_catalan(self):
        loc = Localization("ca")
        self.assertEqual(loc["no_operation"],"res")
        loc["agent_report"]
        loc["book_report"]
        loc["to"]
        loc["from"]

if __name__ == '__main__':
    unittest.main()