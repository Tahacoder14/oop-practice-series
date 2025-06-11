# The base Component interface
class Coffee:
    def get_cost(self):
        return 5
    def get_description(self):
        return "Simple Coffee"

# A Decorator base class (optional but good practice)
class CoffeeDecorator(Coffee):
    def __init__(self, coffee_component):
        self._component = coffee_component

    def get_cost(self):
        return self._component.get_cost()

    def get_description(self):
        return self._component.get_description()

# Concrete Decorators
class WithMilk(CoffeeDecorator):
    def get_cost(self):
        return self._component.get_cost() + 2
    def get_description(self):
        return self._component.get_description() + ", with Milk"

class WithSugar(CoffeeDecorator):
    def get_cost(self):
        return self._component.get_cost() + 1
    def get_description(self):
        return self._component.get_description() + ", with Sugar"

class WithWhippedCream(CoffeeDecorator):
    def get_cost(self):
        return self._component.get_cost() + 3
    def get_description(self):
        return self._component.get_description() + ", with Whipped Cream"