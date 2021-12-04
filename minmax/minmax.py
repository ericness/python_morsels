from typing import Callable, List, Tuple


def minmax(values: List, *, key: Callable = None) -> Tuple:
    """Find the minimum and maximum values in a list.

    Args:
        values (List): List of values
        key (Callable): Function for sorting

    Returns:
        Tuple: Min and max values
    """
    if len(values) == 0:
        raise ValueError("Can't find minimum and maximum of an empty set")
    return min(values, key=key), max(values, key=key)
