import unittest

from classes.room import Room

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room_1 = Room("Plush Paradise", 3)


    def test_room_has_name(self):
        self.assertEqual("Plush Paradise", self.room_1.name)

    def test_room_has_capacity(self):
        self.assertEqual(3, self.room_1.capacity)