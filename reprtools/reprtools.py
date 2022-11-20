from typing import Callable, List, Optional


def format_arguments(*args, **kwargs) -> str:
    """Format arguments into string."""
    result = ""
    for arg in args:
        result += f"'{arg}', " if isinstance(arg, str) else f"{arg}, "
    for key, value in kwargs.items():
        result += f"{key}='{value}', " if isinstance(value, str) else f"{key}={value}, "
    return result.rstrip(", ")


def make_repr(args: Optional[List] = None, kwargs: Optional[List] = None) -> Callable:
    """Generate repr function."""
    args = args if args else []
    kwargs = kwargs if kwargs else []

    def repr(self):
        repr_args = [getattr(self, arg) for arg in args]
        repr_kwargs = {kwarg: getattr(self, kwarg) for kwarg in kwargs}
        result = (
            f"{self.__class__.__name__}({format_arguments(*repr_args, **repr_kwargs)})"
        )
        return result

    return repr
