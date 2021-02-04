import time


class Timer:
    """Time an operation"""

    def __init__(self):
        self.start_time = 0.0
        self.end_time = 0.0
        self.runs = []

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

    @property
    def elapsed(self) -> float:
        return self.end_time - self.start_time
