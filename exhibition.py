# exhibition.py

class Exhibition:
    def __init__(self, name, start_date, end_date, location):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.location = location
        self.artworks = []
        self.tickets_sold = 0
        self.income_generated = 0.0

    def add_artwork(self, artwork):
        self.artworks.append(artwork)

    def remove_artwork(self, artwork):
        self.artworks.remove(artwork)

    def sell_ticket(self, ticket):
        self.tickets_sold += 1
        self.income_generated += ticket.price

    def display_artworks(self):
        print(f"Artworks in the {self.name} exhibition:")
        for artwork in self.artworks:
            print(f"- {artwork.title} by {artwork.artist}")

    def display_financials(self):
        print(f"Total tickets sold for {self.name}: {self.tickets_sold}")
        print(f"Total income from {self.name}: ${self.income_generated}")
