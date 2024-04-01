# tour_ticket.py
from ticket import Ticket

class TourTicket(Ticket):
    def __init__(self, date, price, visitor, tour, language, meeting_point, headset_provided):
        super().__init__(date, price, visitor, tour)
        self.language = language
        self.meeting_point = meeting_point
        self.headset_provided = headset_provided

