# ticket.py

class Ticket:
    def __init__(self, date, price, visitor, event_or_tour):
        self.date = date
        self.price = price
        self.visitor = visitor
        self.event_or_tour = event_or_tour

    def set_price(self, price):
        self.price = price
