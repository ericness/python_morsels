from typing import Iterable, List


class OrderedSet(List):
    """Set collection that keeps element order"""
    def __init__(self, input: Iterable = None):
        self.elements = set()
        if not input:
            return
        for element in input:
            if element not in self:
                self.append(element)
                self.elements.add(element)

    def __repr__(self) -> str:
        return f"OrderedSet({super().__repr__()})" 

    def __contains__(self, o: object) -> bool:
        return o in self.elements

    def __eq__(self, o: object) -> bool:
        if isinstance(o, OrderedSet):
            return super().__eq__(o)
        elif isinstance(o, set):
            return o == self.elements
        elif isinstance(o, list):
            return False
        else:
            return False
