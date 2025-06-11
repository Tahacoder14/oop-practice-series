from abc import ABC, abstractmethod

# The Component Interface
class Part(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    @abstractmethod
    def get_price(self):
        pass

# Leaf objects (individual parts)
class LeafPart(Part):
    def get_price(self):
        return self.price

# Composite object (contains other parts)
class CompositePart(Part):
    def __init__(self, name, price):
        super().__init__(name, price)
        self._sub_parts = []

    def add_part(self, part):
        self._sub_parts.append(part)

    def get_price(self):
        total_price = self.price
        for part in self._sub_parts:
            total_price += part.get_price()
        return total_price