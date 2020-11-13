import unittest

from classes.bar import Bar
# from classes.drink import Drink


class TestBar(unittest.TestCase):
    def setUp(self):
        
        drink_1 = {
            "name" : "Guinness",
            "price": 3
            }
        drink_2 = {
            "name": "Whiskey Sour",
            "price" : 6
            }
        drink_3 = {
            "name": "Tsingtao",
            "price": 4
         }
    

        drinks_list = [drink_1, drink_2, drink_3]

        self.bar = Bar(500, drinks_list)
        

    def test_bar_has_till(self):
        self.assertEqual(500, self.bar.till)

    def test_bar_has_drinks(self):
        self.assertEqual([{
            "name": "Guinness",
            "price": 3
            }, {
            "name": "Whiskey Sour",
            "price" : 6
            }, {
            "name": "Tsingtao",
            "price": 4
         }], self.bar.drinks)

# [Drink("Guiness", 3, 2), Drink("Whiskey Sour", 6, 4), Drink("Tsingtao", 4, 3)]