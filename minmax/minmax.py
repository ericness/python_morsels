from typing import Callable, Iterable, Tuple


def minmax(values: Iterable, *, key: Callable = lambda x: x) -> Tuple:
    """Find the minimum and maximum values in a list.

    Args:
        values (Iterable): List of values
        key (Callable): Function for sorting

    Returns:
        Tuple: Min and max values
    """
    current_min = None
    current_max = None

    for value in values:
        if current_min is None or key(value) < key(current_min):
            current_min = value
        if current_max is None or key(value) > key(current_max):
            current_max = value
    
    if current_min is None and current_max is None:
        raise ValueError("Can't find minimum and maximum of an empty set")
    return current_min, current_max
