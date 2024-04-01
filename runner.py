# runner.py
from datetime import datetime
from artwork import Artwork
from exhibition import Exhibition
from event import Event
from tour import Tour
from visitor import Visitor
from ticket import Ticket
from adult_pricing import AdultPricing
from group_pricing import GroupPricing
from free_pricing import FreePricing
from exhibition_ticket import ExhibitionTicket
from tour_ticket import TourTicket
from event_ticket import EventTicket
from tour_ticket import TourTicket
from guide import Guide
from datetime import datetime, timedelta

def main():
    # Create artworks
    artworks = [
        Artwork("Mona Lisa", "Leonardo da Vinci", datetime(1503, 1, 1), "A masterpiece of the Italian Renaissance", "Permanent"),
        Artwork("The Starry Night", "Vincent Van Gogh", datetime(1889, 6, 19), "An iconic piece of Post-Impressionism", "MoMA"),
        Artwork("The Night Watch", "Rembrandt", datetime(1642, 1, 1), "A notable work of the Dutch Golden Age", "Amsterdam Museum"),
        Artwork("The Birth of Venus", "Sandro Botticelli", datetime(1486, 1, 1), "A celebrated example of early Renaissance art", "Uffizi Gallery"),
        Artwork("Guernica", "Pablo Picasso", datetime(1937, 1, 1), "A powerful anti-war statement", "Reina Sofia Museum")
    ]

    # Set up exhibitions
    exhibitions = [
        Exhibition("Impressionism", datetime(2023, 1, 1), datetime(2023, 12, 31), "Gallery 1"),
        Exhibition("Post-Impressionism", datetime(2023, 1, 1), datetime(2023, 12, 31), "Gallery 2"),
        Exhibition("Dutch Golden Age", datetime(2023, 1, 1), datetime(2023, 12, 31), "Gallery 3"),
        Exhibition("Early Renaissance", datetime(2023, 1, 1), datetime(2023, 12, 31), "Gallery 4"),
        Exhibition("Modernism", datetime(2023, 1, 1), datetime(2023, 12, 31), "Gallery 5")
    ]

    for exhibition in exhibitions:
        for artwork in artworks:
            exhibition.add_artwork(artwork)

    # Create guides
    guides = [
        Guide("John Doe", "G-1001"),
        Guide("Jane Smith", "G-1002"),
        Guide("Emily Jones", "G-1003"),
        Guide("Peter Brown", "G-1004"),
        Guide("Isabella Taylor", "G-1005")
    ]

    # Create tours
    tours = [
        Tour("Impressionism Tour", datetime.now() + timedelta(days=1), 20, guides[0].name, "Gallery 1"),
        Tour("Post-Impressionism Tour", datetime.now() + timedelta(days=2), 20, guides[1].name, "Gallery 2"),
        Tour("Dutch Masters Tour", datetime.now() + timedelta(days=3), 20, guides[2].name, "Gallery 3"),
        Tour("Renaissance Highlights Tour", datetime.now() + timedelta(days=4), 20, guides[3].name, "Gallery 4"),
        Tour("Modernism Tour", datetime.now() + timedelta(days=5), 20, guides[4].name, "Gallery 5")
    ]

    # Set up visitors
    visitors = [
        Visitor("Alice", 28, ),
        Visitor("Bob", 22, ),
        Visitor("Charlie", 35,),
        Visitor("Diana", 42,),
        Visitor("Ethan", 65, )
    ]

    # Define pricing strategies
    pricing_strategies = {
        "adult": AdultPricing(50.0),
        "student": GroupPricing(45.0, 0.1),  
        "senior": FreePricing(),
        "child": FreePricing()  
    }

    # Purchase tickets for each visitor for each exhibition and tour
    for visitor in visitors:
        strategy = pricing_strategies.get(visitor.category, AdultPricing(50.0))
        for exhibition in exhibitions:
            exhibition_ticket_price = strategy.calculate_price(visitor, exhibition)
            exhibition_ticket = ExhibitionTicket(datetime.now(), exhibition_ticket_price, visitor, exhibition, "General", False, False)
            visitor.add_ticket(exhibition_ticket)
            exhibition.sell_ticket(exhibition_ticket)
        
        for tour in tours:
            tour_ticket_price = strategy.calculate_price(visitor, tour)
            tour_ticket = TourTicket(tour.date, tour_ticket_price, visitor, tour, "English", "Main Entrance", True)
            visitor.add_ticket(tour_ticket)
            tour.add_ticket(tour_ticket)

    # Output the details of exhibitions and tours
    for exhibition in exhibitions:
        print(f"Exhibition: {exhibition.name}")
        print("Artworks displayed:")
        for artwork in exhibition.artworks:
            print(f"- {artwork.title} by {artwork.artist}")
        print(f"Total tickets sold: {exhibition.tickets_sold}")
        print(f"Total income from tickets: ${exhibition.income_generated:.2f}\n")

    for tour in tours:
        print(f"Tour: {tour.name} led by Guide: {tour.guide_name}")
        print(f"Total tickets sold: {len(tour.tickets)}")
        print(f"Total income from tickets: ${sum(ticket.price for ticket in tour.tickets):.2f}\n")

    # Print out the tickets each visitor has purchased
    for visitor in visitors:
        print(f"{visitor.name}'s purchased tickets:")
        for ticket in visitor.tickets:
            ticket_type = 'Exhibition Ticket' if isinstance(ticket, ExhibitionTicket) else 'Tour Ticket'
            print(f"- {ticket_type} for {ticket.event_or_tour.name} on {ticket.date} at ${ticket.price:.2f}")
        total_spent = visitor.total_ticket_cost()
        print(f"Total spent on tickets: ${total_spent:.2f}\n")

if __name__ == "__main__":
    main()
