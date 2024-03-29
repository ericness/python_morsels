import copy
from typing import Any, Iterable, Union


class CyclicList:
    """Iterator that loops back to the beginning when exhausted"""
    def __init__(self, iterable: Iterable) -> None:
        self.iterable = list(iterable)
    
    def __iter__(self):
        self.current_index = 0
        return copy.deepcopy(self)
    
    def __next__(self):
        current_index = self.current_index
        self.current_index += 1
        if self.current_index == len(self.iterable):
            self.current_index = 0
        return self.iterable[current_index]

    def __len__(self) -> int:
        return len(self.iterable)
    
    def append(self, element: Any):
        return self.iterable.append(element)
    
    def pop(self, index: int = -1) -> Any:
        return self.iterable.pop(index)

    def __getitem__(self, key: Union[int, slice]) -> Any:
        if isinstance(key, slice):
            start = key.start if key.start else 0
            stop = key.stop if key.stop else 0
            if start == stop == 0:
                stop = len(self)
            return [self[index] for index in range(start, stop)]
        return self.iterable[key % len(self)]

    def __setitem__(self, key: int, value: Any):
        self.iterable[key % len(self)] = value
