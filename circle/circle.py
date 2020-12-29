import math


class Circle:
    """Represents a circle"""

    def __init__(self, radius: int = 1):
        self.radius = radius
        self.diameter = 2 * radius
        self.area = math.pi * radius ** 2

    def __repr__(self) -> str:
        return f"Circle({self.radius})"
