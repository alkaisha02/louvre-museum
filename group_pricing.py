# group_pricing.py
from pricing_strategy import PricingStrategy

class GroupPricing(PricingStrategy):
    def __init__(self, base_price, discount_rate):
        self.base_price = base_price
        self.discount_rate = discount_rate

    def calculate_price(self, visitor, event):
        return self.base_price * (1 - self.discount_rate)  # Apply the discount rate
