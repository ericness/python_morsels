import math
import decimal
from numbers import Number
from typing import SupportsFloat


def is_perfect_square(value: SupportsFloat) -> bool:
    """Determine if number is perfect square"""
    if not isinstance(value, SupportsFloat):
        raise TypeError("Argument is not a number")
    if value < 0:
        return False

    with decimal.localcontext() as c:
        c.prec = 50
        decimal_value = decimal.Decimal(value)
        root = decimal_value.sqrt()
        return root.to_integral_value() ** 2 == decimal_value
