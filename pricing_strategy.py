# pricing_strategy.py
from abc import ABC, abstractmethod

class PricingStrategy(ABC):
    @abstractmethod
    def calculate_price(self, visitor, event):
        pass
