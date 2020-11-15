import unittest

from classes.venue import Venue
from classes.room import Room
from classes.bar import Bar
from classes.drink import Drink

class TestVenue(unittest.TestCase):
    def setUp(self):

        drink_1 = Drink("Guinness", 3, 3)
        drink_2 = Drink("Whiskey Sour", 6, 5)
        drink_3 = Drink("Tsingtao", 4, 3)
        
        drinks_list = [drink_1, drink_2, drink_3]

        room_1 = Room("Plush Paradise", 3)
        bar_1 = Bar(500, drinks_list)

        self.venue_1 = Venue("Cara's OK Karaoke", [room_1], bar_1)


    def test_venue_has_name(self):
        self.assertEqual("Cara's OK Karaoke", self.venue_1.name)