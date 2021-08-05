
from typing import Iterable, List


def window(iterable: Iterable, size: int) -> List:
    """Create tuple windows"""
    pending_results = [[] for _ in range(size)]
    for element in iterable:
        for tup in pending_results:
            tup.append(element)
        current = pending_results.pop(0)
        if len(current) == size:
            yield tuple(current)
        pending_results.append([])
