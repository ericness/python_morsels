from __future__ import annotations

from typing import Union


class float_range:
    def __init__(self, *args):
        self.start = 0.0
        self.step = 1.0
        if len(args) == 0:
            raise TypeError("No arguments")
        if len(args) == 1:
            self.stop = args[0]
        elif len(args) == 2:
            self.start = args[0]
            self.stop = args[1]
        elif len(args) == 3:
            self.start = args[0]
            self.stop = args[1]
            self.step = args[2]
        else:
            raise TypeError("Too many arguments")

    def __iter__(self):
        self.current = self.start
        while (self.current < self.stop and self.step >= 0) or (
            self.current > self.stop and self.step < 0
        ):
            yield self.current
            self.current += self.step

    def __reversed__(self):
        length = len(self)
        self.current = self.start + (length - 1) * self.step
        while (self.current >= self.start and self.step >= 0) or (
            self.current <= self.start and self.step < 0
        ):
            yield self.current
            self.current -= self.step

    def __len__(self):
        length = int((self.stop - self.start) // self.step)
        remainder = (self.stop - self.start) % self.step
        if length < 0:
            return 0
        elif remainder != 0:
            return length + 1
        else:
            return length

    def __eq__(self, other: Union[float_range, range]):
        if isinstance(other, float_range) or isinstance(other, type(range)):
            if len(self) == len(other) == 0:
                return True
            return (
                self.start == other.start
                and self.stop == other.stop
                and self.step == other.step
            )
        return False
