import math

# This violates the open-closed principle

class AreaCalculator:
    def area(self, shape):
        if isinstance(shape, Circle):
            return math.pi * shape.radius ** 2
        elif isinstance(shape, Rectangle):
            return shape.width * shape.height

class Circle:
    def __init__(self, radius) -> None:
        self.radius = radius

class Rectangle:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height


# To fix this

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius) -> None:
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)
    
class Rectangle(Shape):
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
class AreaCalculator:
    def area(self, shape: Shape):
        return shape.area()