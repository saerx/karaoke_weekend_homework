import unittest

from classes.venue import Venue
from classes.room import Room
from classes.bar import Bar
from classes.drink import Drink
from classes.guest import Guest
from classes.song import Song

class TestVenue(unittest.TestCase):
    def setUp(self):

        drink_1 = Drink("Guinness", 3, 3)
        drink_2 = Drink("Whiskey Sour", 6, 5)
        drink_3 = Drink("Tsingtao", 4, 3)
        
        drinks_list = [drink_1, drink_2, drink_3]

        self.room_1 = Room("Plush Paradise", 3)
        self.bar_1 = Bar(500, drinks_list)

        self.venue_1 = Venue("Cara's OK Karaoke", [self.room_1], self.bar_1)

        self.song_1 = Song(10001, "Let's Make Love and Listen to Death from Above", "CSS", [3,30], 2005)
        self.song_2 = Song(10002, "Song 2", "Blur", [2, 2], 1996)
        self.song_3 = Song(10003, "E-Mail My Heart", "Britney Spears", [3, 41], 1999)
        self.song_4 = Song(10004, "Club Tropicana", "Wham!", [4, 28], 1983)
        self.song_5 = Song(10005, "Virtual Insanity", "Jamiroquai", [4, 4], 1996)

        self.guest_1 = Guest("Lovefoxxx", 36, 50, self.song_1)
        self.guest_2 = Guest("Britney Spears", 38, 100, self.song_4)
        self.guest_3 = Guest("Damon Albarn", 52, 20, self.song_3)
        self.guest_4 = Guest("Jamiroquai", 50, 5, self.song_5)
        self.guest_5 = Guest("Human Child", 8, 20, self.song_2)
        self.guest_6 = Guest("Jay-Z", 50, 10000, self.song_5)
        self.guest_7 = Guest("Shania Twain", 55, 80, self.song_1)



    def test_venue_has_name(self):
        self.assertEqual("Cara's OK Karaoke", self.venue_1.name)

    def test_check_in__below_capacity_and_has_enough_money(self):
        self.venue_1.admit_guest(self.guest_1, self.room_1)
        self.venue_1.admit_guest(self.guest_2, self.room_1)
        self.assertEqual([self.guest_1, self.guest_2], self.room_1.guests)

    def test_check_in__below_capacity_and_has_exact_money(self):
        self.venue_1.admit_guest(self.guest_3, self.room_1)
        self.assertEqual([self.guest_3], self.room_1.guests)

    def test_check_in__below_capacity_and_doesnt_have_enough_money(self):
        self.venue_1.admit_guest(self.guest_2, self.room_1)
        self.venue_1.admit_guest(self.guest_4, self.room_1)
        self.assertEqual([self.guest_2], self.room_1.guests)

    def test_check_in__at_capacity(self):
        self.venue_1.admit_guest(self.guest_1, self.room_1)
        self.venue_1.admit_guest(self.guest_2, self.room_1)
        self.venue_1.admit_guest(self.guest_3, self.room_1)
        self.venue_1.admit_guest(self.guest_6, self.room_1)
        self.venue_1.admit_guest(self.guest_7, self.room_1)
        self.assertEqual([self.guest_1, self.guest_2, self.guest_3], self.room_1.guests)

    def test_admit_guest_adds_to_active_rooms_in_bar(self):
        self.venue_1.admit_guest(self.guest_1, self.room_1)
        self.assertEqual(1, len(self.venue_1.bar.active_rooms))