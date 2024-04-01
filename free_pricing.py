# free_pricing.py
from pricing_strategy import PricingStrategy

class FreePricing(PricingStrategy):
    def calculate_price(self, visitor, event):
        return 0  
