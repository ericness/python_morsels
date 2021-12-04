from typing import List, Tuple


def minmax(values: List) -> Tuple:
    """Find the minimum and maximum values in a list.

    Args:
        values (List): List of values

    Returns:
        Tuple: Min and max values
    """
    if len(values) == 0:
        raise ValueError("Can't find minimum and maximum of an empty set")
    return min(values), max(values)
