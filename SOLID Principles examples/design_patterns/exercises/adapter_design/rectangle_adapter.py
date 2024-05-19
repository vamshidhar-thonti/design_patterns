from abc import ABC, abstractmethod

class RectangleLegacy:
    def __init__(self, x, y, w, h) -> None:
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def get_coordinates(self):
        print(f"Reactangle starting at ({self.x}, {self.y}) with width = {self.w} and height = {self.h}")
    
class Rectangle:
    def __init__(self, x1, y1, x2, y2) -> None:
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def get_coordinates(self):
        print(f"Point 1 => ({self.x1}, {self.y1}), Point 2 => ({self.x2}, {self.y2})")

class RectangleAdapter(ABC):
    def __init__(self, legacy_rectangle: RectangleLegacy) -> None:
        self.legacy_rectangle = legacy_rectangle

    @abstractmethod
    def convert(self) -> Rectangle:
        pass

class LegacyRectangleAdapter(RectangleAdapter):
    def convert(self):
        x1 = self.legacy_rectangle.x
        y1 = self.legacy_rectangle.y
        x2 = x1 + self.legacy_rectangle.w
        y2 = y1 - self.legacy_rectangle.h

        return Rectangle(x1, y1, x2, y2)
    
legacy_rectangle = RectangleLegacy(5, 5, 3, 2)
legacy_rectangle.get_coordinates()

rectangle = Rectangle(5, 5, 2, 2)
rectangle.get_coordinates()

rectangle_adapter = LegacyRectangleAdapter(legacy_rectangle)
adapted_rectangle = rectangle_adapter.convert()
adapted_rectangle.get_coordinates()
