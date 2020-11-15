import unittest

from classes.tab import Tab

class TestTab(unittest.TestCase):
    def setUp(self):
        self.tab_1 = Tab("Britney Spears", 50)

    def test_tab_has_name(self):
        self.assertEqual("Britney Spears", self.tab_1.name)

    def test_tab_has_amount(self):
        self.assertEqual(50, self.tab_1.amount)