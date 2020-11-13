class Bar: 
    def __init__(self, till, drinks):
        self.till = till
        self.drinks = drinks
        

    def sell_drink(self, guest, drink):
        if guest.drunkenness < 10:
            self.till += drink.price
            guest.remove_cash(drink["price"])
            guest.increase_drunkenness(drink)