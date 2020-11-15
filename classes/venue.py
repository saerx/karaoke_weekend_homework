from classes.tab import Tab

class Venue:
    def __init__(self, name, rooms, bar):
        self.name = name
        self.rooms = rooms
        self.bar = bar

    
    
    def admit_guest(self, guest, room):
         if guest.wallet >= 10:
            room.check_in(guest)
            self.bar.active_rooms.append(room)
             

