
class Ticket:
    def __init__(self, ticket_type, date, visitor, event):
        self.ticket_type = ticket_type
        self.date = date
        self.visitor = visitor
        self.event = event
        self.price = 0

    def set_price(self, price):
        self.price = price

    def display_ticket(self):
        return f"Type: {self.ticket_type}, Date: {self.date}, Event: {self.event.name}, Price: {self.price}"
