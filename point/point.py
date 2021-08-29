
class Point:
    """Represents a cartesian point"""
    def __init__(self, x: int, y: int, z: int) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y}, z={self.z})"
    
    def __eq__(self, other: object) -> bool:
        return self.x == other.x and self.y == other.y and self.z == other.z