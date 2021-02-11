import time
from statistics import mean, median
from typing import Callable


class Timer():
    """Time an operation"""

    def __init__(self, func: Callable = None):
        self.start_time = 0.0
        self.end_time = 0.0
        self.runs = []
        self.func = func

    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(
        self,
        exc_type: Exception = None,
        exc_value: BaseException = None,
        traceback=None,
    ):
        self.end_time = time.time()
        self.runs.append(self.end_time - self.start_time)

    def __call__(self, *args, **kwargs):
        self.start_time = time.time()
        result = self.func(*args, **kwargs)
        self.end_time = time.time()
        self.runs.append(self.end_time - self.start_time)
        return result

    @property
    def elapsed(self) -> float:
        return self.end_time - self.start_time

    @property
    def min(self) -> float:
        return min(self.runs)

    @property
    def max(self) -> float:
        return max(self.runs)

    @property
    def mean(self) -> float:
        return mean(self.runs)

    @property
    def median(self) -> float:
        return median(self.runs)
