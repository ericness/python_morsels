import warnings
from contextlib import contextmanager
from typing import Type


@contextmanager
def error_on_warnings(message: str = '', category: Type[Warning] = Warning):
    """Raises errors instead of warnings"""
    try:
        warnings.filterwarnings("error", message=message, category=category)
        yield
    finally:
        warnings.resetwarnings()
