class Bar: 
    def __init__(self, till, drinks):
        self.drinks = drinks
        

    def sell_drink(self, guest, room, drink):
       
        if guest.drunkenness < 10:
            guest.remove_cash(drink["price"])
            # guest.increase_drunkenness(drink["alcohol_level"])
            for tab in room.tabs:
                if tab["name"] == guest.name:
                    tab["tab_balance"] += drink["price"]
            

