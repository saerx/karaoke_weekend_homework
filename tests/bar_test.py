import unittest

from classes.bar import Bar


class TestBar(unittest.TestCase):
    def setUp(self):
        self.bar = Bar(500)


    def test_bar_has_till(self):
        self.assertEqual(500, self.bar.till)