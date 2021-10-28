from typing import Any, Iterable, List


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
        if isinstance(o, list) and not isinstance(o, OrderedSet):
            return False
        if isinstance(o, OrderedSet):
            return super().__eq__(o)
        elif isinstance(o, set):
            return o == self.elements
        else:
            return False

    def __ne__(self, o: object) -> bool:
        return not self.__eq__(o)

    def add(self, element: Any):
        if element not in self.elements:
            self.append(element)
            self.elements.add(element)

    def discard(self, element: Any):
        if element in self.elements:
            self.remove(element)
            self.elements.remove(element)
