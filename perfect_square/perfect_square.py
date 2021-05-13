import cmath
import math
import decimal
from numbers import Number
from typing import SupportsFloat


def is_perfect_square(value: SupportsFloat, *, complex: bool = False) -> bool:
    """Determine if number is perfect square"""
    if not complex:
        if not isinstance(value, SupportsFloat):
            raise TypeError("Argument is not a number")
        if value < 0:
            return False

        with decimal.localcontext() as c:
            c.prec = 50
            decimal_value = decimal.Decimal(value)
            root = decimal_value.sqrt()
            return root.to_integral_value() ** 2 == decimal_value
    else:
        root = cmath.sqrt(value)
        return root.real.is_integer() and root.imag.is_integer()
