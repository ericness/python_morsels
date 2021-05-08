import math
from numbers import Number
from typing import SupportsFloat


def is_perfect_square(value: SupportsFloat) -> bool:
    """Determine if number is perfect square"""
    if not isinstance(value, SupportsFloat):
        raise TypeError("Argument is not a number")
    if value < 0:
        return False

    root = math.sqrt(value)
    return math.ceil(root) ** 2 == value or math.floor(root) ** 2 == value
