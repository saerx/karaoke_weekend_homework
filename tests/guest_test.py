import unittest

from classes.guest import Guest 

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest(Lovefoxxx, 36, 50, "Let's Make Love and Listen to Death from Above")
        self.guest_2 = Guest(Britney Spears, 38, 100, "Club Tropicana")
        self.guest_3 = Guest(Damon Albarn, 52, 20, "E-Mail My Heart")
        self.guest_4 = Guest(Jamiroquai, 50, 5, "Virtual Insanity")
        self.guest_5 = Guest(Human Child, 8, 20, "Song 2")