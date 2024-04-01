
# event_ticket.py
from ticket import Ticket

class EventTicket(Ticket):
    def __init__(self, date, price, visitor, event, seat_number, includes_catering, performer_meet_and_greet):
        super().__init__(date, price, visitor, event)
        self.seat_number = seat_number
        self.includes_catering = includes_catering
        self.performer_meet_and_greet = performer_meet_and_greet
