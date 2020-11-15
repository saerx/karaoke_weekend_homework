class Bar: 
    def __init__(self, till, drinks):
        self.drinks = drinks
        

    def find_drink_by_name(self, requested_drink):
         for drink in self.drinks:
            if drink.name == requested_drink:
                return drink

    # def sell_drink(self, guest, room, drink):
    #     if guest.drunkenness < 10:
    #         found_drink = find_drink_by_name(self, drink)
    #         guest.remove_cash(found_drink.price)
    #         # guest.increase_drunkenness(drink["alcohol_level"])
    #         for tab in room.tabs:
    #             if tab["name"] == guest.name:
    #                 tab["tab_balance"] += found_drink.price
            

