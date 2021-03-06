import unittest

from classes.room import Room
from classes.guest import Guest 
from classes.song import Song
from classes.tab import Tab
from classes.bar import Bar
from classes.drink import Drink


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room_1 = Room("Plush Paradise", 3)

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

        drink_1 = Drink("Guinness", 3, 3)
        drink_2 = Drink("Whiskey Sour", 6, 5)
        drink_3 = Drink("Tsingtao", 4, 3)
        
        drinks_list = [drink_1, drink_2, drink_3]

        self.bar_1 = Bar(500, drinks_list)

        
    def test_room_has_name(self):
        self.assertEqual("Plush Paradise", self.room_1.name)

    def test_room_has_capacity(self):
        self.assertEqual(3, self.room_1.capacity)

    def test_check_in__below_capacity(self):
        self.room_1.check_in(self.guest_1)
        self.room_1.check_in(self.guest_2)
        self.assertEqual([self.guest_1, self.guest_2], self.room_1.guests)

    # def test_check_in__below_capacity_and_has_exact_money(self):
    #     self.room_1.check_in(self.guest_3)
    #     self.assertEqual([self.guest_3], self.room_1.guests)

    # def test_check_in__below_capacity_and_doesnt_have_enough_money(self):
    #     self.room_1.check_in(self.guest_2)
    #     self.room_1.check_in(self.guest_4)
    #     self.assertEqual([self.guest_2], self.room_1.guests)

    def test_check_in__at_capacity(self):
        self.room_1.check_in(self.guest_1)
        self.room_1.check_in(self.guest_2)
        self.room_1.check_in(self.guest_3)
        self.room_1.check_in(self.guest_6)
        self.room_1.check_in(self.guest_7)
        self.assertEqual([self.guest_1, self.guest_2, self.guest_3], self.room_1.guests)

    def test_check_out(self):
        self.room_1.check_in(self.guest_3)
        self.room_1.check_in(self.guest_6)
        self.room_1.check_out(self.guest_3)
        self.assertEqual([self.guest_6], self.room_1.guests)

    def test_add_songs__list(self):
        computer_songs_playlist = [self.song_1, self.song_3]
        self.room_1.add_songs(computer_songs_playlist)
        self.assertEqual([self.song_1, self.song_3], self.room_1.songs)

    def test_add_songs__single_song(self):
        self.room_1.add_songs(self.song_4)
        self.assertEqual([self.song_4], self.room_1.songs)

    def test_add_songs__both(self):
        computer_songs_playlist = [self.song_1, self.song_3]
        self.room_1.add_songs(computer_songs_playlist)
        self.room_1.add_songs(self.song_4)
        self.assertEqual([self.song_1, self.song_3, self.song_4], self.room_1.songs)

    def test_add_songs__not_song(self):
        self.room_1.add_songs("cool song")
        self.assertEqual([], self.room_1.songs)

    def test_tabs_start_at_zero(self):
        self.assertEqual(self.room_1.tabs, [])

    def test_check_in_changes_tab(self):
        self.room_1.check_in(self.guest_1)
        self.room_1.check_in(self.guest_2)
        self.assertEqual(len(self.room_1.tabs), 2)
        self.assertIsInstance(self.room_1.tabs[0], Tab)

   
    



    