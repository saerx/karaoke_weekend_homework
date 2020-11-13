import unittest

from classes.bar import Bar
from classes.guest import Guest
from classes.room import Room
from classes.song import Song
# from classes.drink import Drink


class TestBar(unittest.TestCase):
    def setUp(self):
        
        drink_1 = {
            "name" : "Guinness",
            "price": 3,
            "alcohol_level" : 3
            }
        drink_2 = {
            "name": "Whiskey Sour",
            "price" : 6,
            "alcohol_level" : 5
            }
        drink_3 = {
            "name": "Tsingtao",
            "price": 4,
            "alcohol_level" : 3
            }

    
        drinks_list = [drink_1, drink_2, drink_3]

        self.bar = Bar(500, drinks_list)

        self.song_1 = Song(10001, "Let's Make Love and Listen to Death from Above", "CSS", [3,30], 2005)
        self.song_4 = Song(10004, "Club Tropicana", "Wham!", [4, 28], 1983)

        self.guest_1 = Guest("Lovefoxxx", 36, 50, self.song_1)
        self.guest_2 = Guest("Britney Spears", 38, 100, self.song_4)

        self.room_1 = Room("Plush Paradise", 3)

    

    def test_bar_has_drinks(self):
        self.assertEqual([{
            "name" : "Guinness",
            "price": 3,
            "alcohol_level" : 3
            }, {
            "name": "Whiskey Sour",
            "price" : 6,
            "alcohol_level" : 5
            }, {
            "name": "Tsingtao",
            "price": 4,
            "alcohol_level" : 3
            }], self.bar.drinks)

# [Drink("Guiness", 3, 2), Drink("Whiskey Sour", 6, 4), Drink("Tsingtao", 4, 3)]

    def test_sell_drink(self):
        self.room_1.check_in(self.guest_1)
        self.bar.sell_drink(self.guest_1, self.room_1, self.bar.drinks[0])
        self.assertEqual(37, self.guest_1.wallet)
        # self.assertEqual(3, guest.drunkenness)
        self.assertEqual(13, self.room_1.tabs[0]["tab_balance"])
