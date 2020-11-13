import unittest

from classes.room import Room
from classes.guest import Guest 


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room_1 = Room("Plush Paradise", 3)

        self.guest_1 = Guest("Lovefoxxx", 36, 50, "Let's Make Love and Listen to Death from Above")
        self.guest_2 = Guest("Britney Spears", 38, 100, "Club Tropicana")
        self.guest_3 = Guest("Damon Albarn", 52, 20, "E-Mail My Heart")
        self.guest_4 = Guest("Jamiroquai", 50, 5, "Virtual Insanity")
        self.guest_5 = Guest("Human Child", 8, 20, "Song 2")


    def test_room_has_name(self):
        self.assertEqual("Plush Paradise", self.room_1.name)

    def test_room_has_capacity(self):
        self.assertEqual(3, self.room_1.capacity)

    def test_check_in(self):
        self.room_1.check_in(self.guest_1)
        self.room_1.check_in(self.guest_2)
        self.assertEqual([self.guest_1, self.guest_2], self.room_1.guests)

    def test_check_out(self):
        self.room_1.check_in(self.guest_3)
        self.room_1.check_in(self.guest_4)
        self.room_1.check_out(self.guest_3)
        self.assertEqual([self.guest_4], self.room_1.guests)