import unittest

from classes.song import Song 

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song_1 = Song(10001, "Club Tropicana", "Wham!", [4, 28], 1983)
        self.song_2 = Song(10002, "Let's Make Love and Listen to Death from Above", "CSS", [3,30], 2005)
        self.song_3 = Song(10003, "E-Mail My Heart", "Britney Spears", [3, 41], 1999)