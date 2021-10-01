import itertools
import math
from typing import Iterable


def chunked(sequence: Iterable, n: int):
    """Chunk elements into lists"""
    nested = []
    i = 0
    for element in sequence:
        nested.append(element)
        i += 1
        if i == n:
            i = 0
            yield nested
            nested = []
    if nested:
        yield nested
