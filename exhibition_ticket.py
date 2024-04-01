# exhibition_ticket.py
from ticket import Ticket

class ExhibitionTicket(Ticket):
    def __init__(self, date, price, visitor, exhibition, access_level, audio_guide_included, souvenir_booklet_included):
        super().__init__(date, price, visitor, exhibition)
        self.access_level = access_level
        self.audio_guide_included = audio_guide_included
        self.souvenir_booklet_included = souvenir_booklet_included
