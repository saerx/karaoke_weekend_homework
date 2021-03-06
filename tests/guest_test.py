import unittest

from classes.guest import Guest 
from classes.room import Room
from classes.song import Song

class TestGuest(unittest.TestCase):
    def setUp(self):
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

        self.room_1 = Room("Plush Paradise", 3)

        self.drink_1 = {
            "name" : "Guinness",
            "price": 3,
            "alcohol_level" : 3
            }


    def test_guest_has_name(self):
        self.assertEqual("Lovefoxxx", self.guest_1.name)

    def test_guest_has_age(self):
        self.assertEqual(38, self.guest_2.age)

    def test_guest_has_wallet(self):
        self.assertEqual(5, self.guest_4.wallet)

    def test_guest_has_favourite_song(self):
        self.assertEqual(self.song_3, self.guest_3.favourite_song)

    def test_check_song_on_playlist__song_on_playlist(self):
        big_playlist = [self.song_1, self.song_2, self.song_3, self.song_4]
        self.room_1.add_songs(big_playlist)
        self.room_1.check_in(self.guest_2)
        result = self.guest_2.check_song_on_playlist(self.room_1)
        self.assertEqual(f"They have {self.guest_2.favourite_song.title}! Alright!", result)

    def test_check_song_on_playlist__song_not_on_playlist(self):
        big_playlist = [self.song_1, self.song_2, self.song_3, self.song_4]
        self.room_1.add_songs(big_playlist)
        self.room_1.check_in(self.guest_6)
        result = self.guest_6.check_song_on_playlist(self.room_1)
        self.assertIsNone(result)

    def test_check_song_on_playlist__song_on_playlist_guest_not_in_room(self):
        big_playlist = [self.song_1, self.song_2, self.song_3, self.song_4]
        self.room_1.add_songs(big_playlist)
        result = self.guest_2.check_song_on_playlist(self.room_1)
        self.assertIsNone(result)
    
    def test_remove_cash(self):
        value = self.drink_1["price"]
        self.guest_2.remove_cash(value)
        self.assertEqual(97, self.guest_2.wallet)

    def test_increase_drunkenness(self):
        self.guest_2.increase_drunkenness(self.drink_1)
        self.guest_2.increase_drunkenness(self.drink_1)
        self.assertEqual(6, self.guest_2.drunkenness)

  

