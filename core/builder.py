# The Product
class Car:
    """The complex object we want to create."""
    def __init__(self):
        self.engine = None
        self.wheels = None
        self.color = None

    def __str__(self):
        return f"Car specs: Engine - {self.engine}, Wheels - {self.wheels}, Color - {self.color}"

# The Abstract Builder
class CarBuilder:
    """The abstract interface for creating parts of the Product."""
    def __init__(self):
        self.car = Car()
    def set_engine(self, engine_type):
        pass
    def set_wheels(self, wheel_type):
        pass
    def set_color(self, color):
        pass
    def get_car(self):
        return self.car

# Concrete Builder
class SportsCarBuilder(CarBuilder):
    """
    Implements the Builder interface to construct and assemble the parts.
    Uses a 'fluent interface' by returning 'self' to allow for chaining.
    """
    def set_engine(self, engine_type):
        self.car.engine = engine_type
        return self
    def set_wheels(self, wheel_type):
        self.car.wheels = wheel_type
        return self
    def set_color(self, color):
        self.car.color = color
        return self

# The Director (Optional, can be used to encapsulate common build processes)
class Director:
    def __init__(self, builder):
        self._builder = builder

    def build_standard_car(self, color):
        return self._builder.set_engine("V8").set_wheels("18-inch Alloy").set_color(color).get_car()

    def build_custom_car(self, engine, wheels, color):
        return self._builder.set_engine(engine).set_wheels(wheels).set_color(color).get_car()
