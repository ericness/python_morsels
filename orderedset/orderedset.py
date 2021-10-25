from typing import Iterable, List


class OrderedSet(List):
    """Set collection that keeps element order"""
    def __init__(self, input: Iterable = None):
        if not input:
            return
        for element in input:
            if element not in self:
                self.append(element)

    def __repr__(self) -> str:
        return f"OrderedSet({super().__repr__()})" 
