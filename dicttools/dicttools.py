import copy
from typing import Any, Dict

DEFAULT = object()


def pluck(data: Dict[Any, Any], *paths, sep: str = ".", default: Any = DEFAULT) -> Any:
    """Retrieve element at path of nested dicts.

    Args:
        data (Dict[Any, Any]): Nested dicts.
        paths (str): Paths of keys to traverse.
        sep (str): Separator of path components.
        default (Any): Value to return on error.

    Returns:
        Any: Objects at path locations.
    """
    result = []
    for path in paths:
        key_error = False
        keys = path.split(sep)
        loop_data = copy.deepcopy(data)

        for key in keys:
            try:
                loop_data = loop_data[key]
            except KeyError as ex:
                if default is not DEFAULT:
                    result.append(default)
                    key_error = True
                    break
                raise ex
        if not key_error:
            result.append(loop_data)

    return result[0] if len(result) == 1 else tuple(result)
