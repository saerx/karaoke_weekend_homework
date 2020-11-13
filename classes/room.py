class Room:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.songs = []
        self.guests = []


    def check_in(self, guest):
        self.guests.append(guest) 

    def check_out(self, guest):
        self.guests.remove(guest)

    def add_songs(self, song_or_playlist):
        if isinstance(song_or_playlist, list):
            self.songs.extend(song_or_playlist)
        else:
            self.songs.append(song_or_playlist)