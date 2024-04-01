# tour.py

class Tour:
    def __init__(self, name, date, group_size, guide_name, location):
        self.name = name
        self.date = date
        self.group_size = group_size
        self.guide_name = guide_name
        self.location = location
        self.tickets = []

    def add_ticket(self, ticket):
        if len(self.tickets) < self.group_size:
            self.tickets.append(ticket)
        else:
            raise Exception("Tour is full.")

    def is_full(self):
        return len(self.tickets) >= self.group_size
