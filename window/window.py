
from typing import Iterable, List


def window(iterable: Iterable, size: int) -> List:
    """Create tuple windows"""
    result = []
    for i in range(len(iterable) - size + 1):
        result.append(tuple(iterable[i:i+size]))
    return result
