from numbers import Number
from typing import Union, Iterable


def deep_add(values: Union[Iterable, Number], start: Number = 0) -> Number:
    """Adds all numbers in nested iterable structure"""
    if isinstance(values, Number):
        return values
    else:
        return sum([deep_add(value) for value in values], start=start)
