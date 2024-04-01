# adult_pricing.py
from pricing_strategy import PricingStrategy

class AdultPricing(PricingStrategy):
    def __init__(self, base_price):
        self.base_price = base_price

    def calculate_price(self, visitor, event):
        return self.base_price  # This could be more complex based on discounts, etc.
