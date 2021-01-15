from typing import Sequence, Iterable


def compact(values: Sequence) -> Iterable:
    result = []
    for value in values:
        if not 'last' in locals() or not value == last or (value is None and last is None):
            result.append(value)
        last = value
    return result
