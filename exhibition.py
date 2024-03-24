# exhibition.py
class Exhibition:
    def __init__(self, name, start_date, end_date, location):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.location = location
        self.artworks = []
        self.tickets_sold = []

    def add_artwork(self, artwork):
        self.artworks.append(artwork)

    def remove_artwork(self, artwork):
        self.artworks.remove(artwork)

    def add_ticket_sold(self, ticket):
        self.tickets_sold.append(ticket)

    def calculate_earnings(self):
        return sum(ticket.price for ticket in self.tickets_sold)

    def is_ongoing(self):
        from datetime import date
        return self.start_date <= date.today() <= self.end_date
