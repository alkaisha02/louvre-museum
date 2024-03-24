# runner.py
from datetime import date
from artwork import Artwork
from exhibition import Exhibition
from event import Event
from visitor import Visitor
from ticket import Ticket
from pricing_strategy import AdultPricing, ChildPricing, GroupPricing

def main():
    # Create artworks
    mona_lisa = Artwork("Mona Lisa", "Leonardo da Vinci", date(1503, 1, 1), "Renaissance masterpiece", "Permanent Gallery")
    starry_night = Artwork("Starry Night", "Vincent van Gogh", date(1889, 1, 1), "Post-Impressionist masterpiece", "Permanent Gallery")

    # Create an exhibition and add artworks
    renaissance_exhibition = Exhibition("Renaissance Art", date(2023, 1, 1), date(2023, 12, 31), "Main Hall")
    renaissance_exhibition.add_artwork(mona_lisa)

    # Create an event
    concert_event = Event("Concert", date(2023, 6, 15), "Outdoor Stage", 100)

    # Create visitors
    adult_visitor = Visitor("John Doe", 30, "adult")
    child_visitor = Visitor("Jane Doe", 10, "child")
    group_visitor = Visitor("Group Tour", 35, "group")

    # Create tickets for the event
    adult_ticket = Ticket("event", date(2023, 6, 15), adult_visitor, concert_event)
    child_ticket = Ticket("event", date(2023, 6, 15), child_visitor, concert_event)
    group_ticket = Ticket("event", date(2023, 6, 15), group_visitor, concert_event)

    # Set ticket prices using pricing strategies
    adult_pricing = AdultPricing()
    child_pricing = ChildPricing()
    group_pricing = GroupPricing()

    adult_ticket.set_price(adult_pricing.calculate_price(adult_visitor, concert_event))
    child_ticket.set_price(child_pricing.calculate_price(child_visitor, concert_event))
    group_ticket.set_price(group_pricing.calculate_price(group_visitor, concert_event))

    # Add tickets to visitors
    adult_visitor.add_ticket(adult_ticket)
    child_visitor.add_ticket(child_ticket)
    group_visitor.add_ticket(group_ticket)

    # Display ticket details
    print(adult_ticket.display_ticket())
    print(child_ticket.display_ticket())
    print(group_ticket.display_ticket())

    # Display total ticket cost for each visitor
    print(f"Total cost for {adult_visitor.name}: {adult_visitor.total_ticket_cost()}")
    print(f"Total cost for {child_visitor.name}: {child_visitor.total_ticket_cost()}")
    print(f"Total cost for {group_visitor.name}: {group_visitor.total_ticket_cost()}")

    # Check if the exhibition is ongoing
    print(f"Is the {renaissance_exhibition.name} exhibition ongoing? {renaissance_exhibition.is_ongoing()}")

    # Calculate earnings from ticket sales for the exhibition
    renaissance_exhibition.add_ticket_sold(adult_ticket)
    renaissance_exhibition.add_ticket_sold(child_ticket)
    renaissance_exhibition.add_ticket_sold(group_ticket)
    print(f"Earnings from the {renaissance_exhibition.name} exhibition: {renaissance_exhibition.calculate_earnings()}")

    # List events for a visitor
    print(f"Events attended by {adult_visitor.name}: {adult_visitor.list_events()}")

    # Update artwork's historical significance
    mona_lisa.update_historical_significance("One of the most recognizable pieces of art in the world")
    print(f"Updated historical significance of {mona_lisa.title}: {mona_lisa.historical_significance}")

    # Calculate the age of an artwork
    print(f"Age of {starry_night.title}: {starry_night.calculate_age()} years")

if __name__ == "__main__":
    main()
