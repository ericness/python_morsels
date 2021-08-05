import itertools
from typing import Iterable, Iterator

DUMMY = "__no_value__"

def interleave(iterable1: Iterable, iterable2: Iterable) -> Iterator:
    """Interleave the elements of multiple iterables"""
    for element1, element2 in itertools.zip_longest(iterable1, iterable2, fillvalue=DUMMY):
       if element1 != DUMMY:
            yield element1
       if element2 != DUMMY:
            yield element2

if __name__ == "__main__":
    result = interleave([], [])
    print(result)
