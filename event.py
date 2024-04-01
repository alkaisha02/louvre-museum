# event.py
from exhibition import Exhibition

class Event(Exhibition):
    def __init__(self, name, start_date, end_date, location, event_type):
        super().__init__(name, start_date, end_date, location)
        self.event_type = event_type
        self.ticket_price = None  

    def set_ticket_price(self, price):
        self.ticket_price = price
