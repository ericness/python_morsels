import itertools
import math
from typing import Sequence


def chunked(sequence: Sequence, n: int):
    """Chunk elements into lists"""
    return [
        itertools.islice(sequence, i * n, i * n + n)
        for i in range(math.ceil(len(sequence) / n))
    ]
