# visitor.py

class Visitor:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.category = self.determine_category(age)
        self.tickets = []

    def add_ticket(self, ticket):
        self.tickets.append(ticket)

    def total_ticket_cost(self):
        return sum(ticket.price for ticket in self.tickets)

    @staticmethod
    def determine_category(age):
        if age < 18:
            return "child"
        elif age < 60:
            return "adult"
        else:
            return "senior"
