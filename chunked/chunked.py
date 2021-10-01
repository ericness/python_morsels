import itertools
import math
from typing import Iterable


def chunked(sequence: Iterable, n: int):
    """Chunk elements into lists"""
    result = []
    nested = []
    i = 0
    for element in sequence:
        nested.append(element)
        i += 1
        if i == n:
            i = 0
            result.append(nested)
            nested = []
    if nested:
        result.append(nested)
    return result
