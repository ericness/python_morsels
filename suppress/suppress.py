from contextlib import ContextDecorator
from dataclasses import dataclass
from types import TracebackType
from typing import Tuple, Optional 


@dataclass
class ContextReturn:
    """Returned from context class"""
    exception: Optional[BaseException]
    traceback: Optional[TracebackType]


class suppress(ContextDecorator):
    """Suppress a selected exception within a context"""
    def __init__(self, *exc_types: Tuple[Exception]):
        self.exc_types = exc_types
        self.context_return = ContextReturn(None, None)
    
    def __enter__(self):
        return self.context_return
    
    def __exit__(self, exc_type: Exception, exc_value: BaseException, traceback) -> bool:
        is_in_types = type(exc_value) in self.exc_types
        is_in_subtypes = any([issubclass(type(exc_value), t) for t in self.exc_types])
        if is_in_types or is_in_subtypes:
            self.context_return.exception = exc_value
            self.context_return.traceback = traceback
            return True
        elif exc_value:
            raise exc_value
        return True
 