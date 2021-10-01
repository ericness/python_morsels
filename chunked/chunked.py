import itertools
import math
from typing import Iterable, Any

FILL = object()


def chunked(sequence: Iterable, n: int, *, fill: Any = FILL):
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
        if fill != FILL:
            for _ in range(n - len(nested)):
                nested.append(fill)
        yield nested
