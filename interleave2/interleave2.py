import itertools
from typing import Iterable, Iterator

DUMMY = "__no_value__"

def interleave(*iterable_args) -> Iterator:
    """Interleave the elements of multiple iterables"""
    for elements in itertools.zip_longest(*iterable_args, fillvalue=DUMMY):
         for element in elements:
             if element != DUMMY:
                 yield element
