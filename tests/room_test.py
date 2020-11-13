import unittest

from classes.room import Room
from classes.guest import Guest 
from classes.song import Song


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room_1 = Room("Plush Paradise", 3)

        self.guest_1 = Guest("Lovefoxxx", 36, 50, "Let's Make Love and Listen to Death from Above")
        self.guest_2 = Guest("Britney Spears", 38, 100, "Club Tropicana")
        self.guest_3 = Guest("Damon Albarn", 52, 20, "E-Mail My Heart")
        self.guest_4 = Guest("Jamiroquai", 50, 5, "Virtual Insanity")
        self.guest_5 = Guest("Human Child", 8, 20, "Song 2")
        self.guest_6 = Guest("Jay-Z", 50, 10000, "That Don't Impress Me Much")
        self.guest_7 = Guest("Shania Twain", 55, 80, "Avril 14")

        self.song_1 = Song(10001, "Let's Make Love and Listen to Death from Above", "CSS", [3,30], 2005)
        self.song_2 = Song(10002, "Song 2", "Blur", [2, 2], 1996)
        self.song_3 = Song(10003, "E-Mail My Heart", "Britney Spears", [3, 41], 1999)
        self.song_4 = Song(10004, "Club Tropicana", "Wham!", [4, 28], 1983)



    def test_room_has_name(self):
        self.assertEqual("Plush Paradise", self.room_1.name)

    def test_room_has_capacity(self):
        self.assertEqual(3, self.room_1.capacity)

    def test_check_in__below_capacity(self):
        self.room_1.check_in(self.guest_1)
        self.room_1.check_in(self.guest_2)
        self.assertEqual([self.guest_1, self.guest_2], self.room_1.guests)

    def test_check_in__at_capacity(self):
        self.room_1.check_in(self.guest_1)
        self.room_1.check_in(self.guest_2)
        self.room_1.check_in(self.guest_3)
        self.room_1.check_in(self.guest_6)
        self.room_1.check_in(self.guest_7)
        self.assertEqual([self.guest_1, self.guest_2, self.guest_3], self.room_1.guests)

    def test_check_out(self):
        self.room_1.check_in(self.guest_3)
        self.room_1.check_in(self.guest_4)
        self.room_1.check_out(self.guest_3)
        self.assertEqual([self.guest_4], self.room_1.guests)

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

    