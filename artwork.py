# artwork.py

class Artwork:
    def __init__(self, title, artist, creation_date, historical_significance, location):
        self.title = title
        self.artist = artist
        self.creation_date = creation_date
        self.historical_significance = historical_significance
        self.location = location

    def update_historical_significance(self, new_significance):
        self.historical_significance = new_significance

    def get_details(self):
        return f"{self.title} by {self.artist}, created on {self.creation_date}"
