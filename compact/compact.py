from typing import Sequence, Iterable


def compact(values: Sequence) -> Iterable:
    for value in values:
        if not 'last' in locals() or not value == last or (value is None and last is None):
            yield value
        last = value
