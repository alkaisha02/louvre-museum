
class PricingStrategy:
    def calculate_price(self, visitor, event):
        pass

    def describe_strategy(self):
        return "Base pricing strategy"

class AdultPricing(PricingStrategy):
    def calculate_price(self, visitor, event):
        return event.ticket_price

    def describe_strategy(self):
        return "Standard adult pricing"

class ChildPricing(PricingStrategy):
    def calculate_price(self, visitor, event):
        return 0

    def describe_strategy(self):
        return "Free entry for children"

class GroupPricing(PricingStrategy):
    def calculate_price(self, visitor, event):
        return event.ticket_price * 0.5

    def describe_strategy(self):
        return "50% discount for groups"
