from typing import Dict, Any, KeysView, ItemsView, ValuesView, Iterator


class ProxyDict:
    def __init__(self, source_dict: Dict):
        self.wrapped_dict = source_dict
    
    def __getitem__(self, key: Any) -> Any:
        return self.wrapped_dict[key]
    
    def __setitem__(self, key: Any, new: Any):
        raise TypeError("'ProxyDict' object does not support item assignment")

    def keys(self) -> KeysView:
        return self.wrapped_dict.keys()

    def __len__(self) -> int:
        return len(self.wrapped_dict)

    def items(self) -> ItemsView:
        return self.wrapped_dict.items()

    def values(self) -> ValuesView:
        return self.wrapped_dict.values()

    def get(self, key: Any, default: Any = None) -> Any:
        try:
            value = self.wrapped_dict[key]
            return value
        except KeyError:
            return default

    def __iter__(self) -> Iterator:
        return iter(self.wrapped_dict)

    def __repr__(self) -> str:
        return f"ProxyDict({self.wrapped_dict})"
