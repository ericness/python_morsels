from typing import Iterable, Generator


def interleave(iterable1: Iterable, iterable2: Iterable) -> Generator:
    """Return a generator of interleaved elements of both iterables"""
    length1 = len(iterable1)
    length2 = len(iterable2)

    for index in range(max([length1, length2])):
        if index < length1:
            yield iterable1[index]
        if index < length2:
            yield iterable2[index]
