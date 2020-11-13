class Bar: 
    def __init__(self, till, drinks):
        self.till = till
        self.drinks = drinks
        

    def find_guest_tab(self, guest, room):
        for tab in room.tabs:
            if tab["name"] == guest.name:
                return tab["tab_balance"]

    # def sell_drink(self, guest, drink):
       
    #     if guest.drunkenness < 10:
    #         self.till += drink.price
    #         guest.remove_cash(drink["price"])
    #         guest.increase_drunkenness(drink["alcohol_level"])
    #         new_tab["tab"] += drink["price"]
