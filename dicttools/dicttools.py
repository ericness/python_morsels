from typing import Any, Dict


def pluck(data: Dict[Any, Any], path: str, sep: str = ".") -> Any:
    """Retrieve element at path of nested dicts.

    Args:
        data (Dict[Any, Any]): Nested dicts.
        path (str): Path of keys to traverse.

    Returns:
        Any: Object at path location.
    """
    keys = path.split(sep)
    result = data

    for key in keys:
        result = result[key]

    return result
