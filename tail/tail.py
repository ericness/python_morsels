from typing import List, Sequence


def tail(seq: Sequence, n: int) -> List:
    if n <= 0:
        return []
    return list(seq[-n:])
