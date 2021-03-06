from classes.song import Song
from classes.tab import Tab
from classes.bar import Bar

class Room:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.songs = []
        self.guests = []
        self.tabs = []


    def check_in(self, guest):
        if len(self.guests) < self.capacity:
            self.guests.append(guest)
            new_tab = Tab(guest.name, 10)
            guest.remove_cash(10)
            self.tabs.append(new_tab) 

    def check_out(self, guest):
        self.guests.remove(guest)

    def add_songs(self, song_or_playlist):
        if isinstance(song_or_playlist, list):
            self.songs.extend(song_or_playlist)
        elif isinstance(song_or_playlist, Song):
            self.songs.append(song_or_playlist)