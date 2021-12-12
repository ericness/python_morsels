from typing import Any, Callable


class count_calls:
    def __init__(self, func: Callable = None) -> None:
        self.calls = 0
        self.func = func
    
    def __call__(self) -> Any:
        self.calls += 1
        if self.func:
            return self.func()
