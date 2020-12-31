import math


class Circle:
    """Represents a circle"""

    def __init__(self, radius: int = 1):
        self.radius = radius

    @property
    def radius(self) -> int:
        return self._radius

    @radius.setter
    def radius(self, radius: int):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = radius

    @property
    def diameter(self) -> int:
        return self.radius * 2

    @diameter.setter
    def diameter(self, diameter: int):
        self.radius = diameter / 2

    @property
    def area(self) -> float:
        return math.pi * self.radius ** 2

    def __repr__(self) -> str:
        return f"Circle({self.radius})"
