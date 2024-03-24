
class Visitor:
    def __init__(self, name, age, category):
        self.name = name
        self.age = age
        self.category = category
        self.tickets = []

    def add_ticket(self, ticket):
        self.tickets.append(ticket)

    def remove_ticket(self, ticket):
        self.tickets.remove(ticket)

    def total_ticket_cost(self):
        return sum(ticket.price for ticket in self.tickets)

    def list_events(self):
        return [ticket.event.name for ticket in self.tickets]