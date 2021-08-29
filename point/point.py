from __future__ import annotations

class Point:
    """Represents a cartesian point"""
    def __init__(self, x: int, y: int, z: int) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y}, z={self.z})"
    
    def __eq__(self, other: Point) -> bool:
        return self.x == other.x and self.y == other.y and self.z == other.z
    
    def __add__(self, other: Point) -> Point:
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: Point) -> Point:
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scale: int) -> Point:
        return Point(self.x * scale, self.y * scale, self.z * scale)

    def __rmul__(self, scale:int) -> Point:
        return self * scale

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z
