class Guest:
    def __init__(self, name, age, wallet, favourite_song):
        self.name = name
        self.age = age
        self.wallet = wallet
        self.favourite_song = favourite_song
        self.drunkenness = 0


    def check_song_on_playlist(self, room):
        if room.guests.count(self) == 1 and room.songs.count(self.favourite_song) > 0:
            return f"They have {self.favourite_song.title}! Alright!"

    def remove_cash(self, value):
        self.wallet -= value

    def increase_drunkenness(self, drink):
        self.drunkenness += drink["alcohol_level"]


