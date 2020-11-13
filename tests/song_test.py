import unittest

from classes.song import Song 

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song_1 = Song(10001, "Let's Make Love and Listen to Death from Above", "CSS", [3,30], 2005)
        self.song_2 = Song(10002, "Song 2", "Blur", [2, 2], 1996)
        self.song_3 = Song(10003, "E-Mail My Heart", "Britney Spears", [3, 41], 1999)
        self.song_4 = Song(10004, "Club Tropicana", "Wham!", [4, 28], 1983)


    def test_song_has_code_num(self):
        self.assertEqual(10001, self.song_1.code_num)

    def test_song_has_title(self):
        self.assertEqual("Song 2", self.song_2.title)

    def test_song_has_artist(self):
        self.assertEqual("Wham!", self.song_4.artist)

    def test_song_has_run_time(self):
        self.assertEqual([4, 28], self.song_4.run_time)

    def test_song_has_year(self):
        self.assertEqual(1999, self.song_3.year)