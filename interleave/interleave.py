from typing import Iterable, Generator


def interleave(iterable1: Iterable, iterable2: Iterable) -> Generator:
    """Return a generator of interleaved elements of both iterables"""
    # length1 = len(iterable1)
    # length2 = len(iterable2)
    iter1_done = False
    iter2_done = False
    iter1 = iter(iterable1)
    iter2 = iter(iterable2)
    while not iter1_done or not iter2_done:
        try:
            yield next(iter1)
        except StopIteration:
            iter1_done = True

        try:
            yield next(iter2)
        except StopIteration:
            iter2_done = True
