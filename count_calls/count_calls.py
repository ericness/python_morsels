from typing import Any, Callable


class count_calls:
    def __init__(self, func: Callable = None) -> None:
        self.calls = 0
        self.func = func
        if func:
            self.__module__ = func.__module__
            self.__name__ = func.__name__
            self.__qualname__ = func.__qualname__
            self.__doc__ = func.__doc__
            self.__annotations__ = func.__annotations__

    def __call__(self, *args, **kwargs) -> Any:
        self.calls += 1
        if self.func:
            return self.func(*args, **kwargs)

    def __repr__(self) -> str:
        if self.func:
            return self.func.__repr__()
        else:
            super().__repr__()
