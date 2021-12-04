from typing import Callable, Iterable, Tuple


def minmax(values: Iterable, *, key: Callable = lambda x: x) -> Tuple:
    """Find the minimum and maximum values in a list.

    Args:
        values (Iterable): List of values
        key (Callable): Function for sorting

    Returns:
        Tuple: Min and max values
    """
    min_value = None
    max_value = None
    min_key = None
    max_key = None

    for current_value in values:
        current_key = key(current_value)
        if min_value is None or current_key < min_key:
            min_value = current_value
            min_key = current_key
        if max_value is None or current_key > max_key:
            max_value = current_value
            max_key = current_key

    if min_value is None and max_value is None:
        raise ValueError("Can't find minimum and maximum of an empty set")
    return min_value, max_value
