from typing import Dict, Any, KeysView


class ProxyDict:
    def __init__(self, source_dict: Dict):
        self.wrapped_dict = source_dict
    
    def __getitem__(self, key: Any) -> Any:
        return self.wrapped_dict[key]
    
    def __setitem__(self, key: Any, new: Any):
        raise TypeError("'ProxyDict' object does not support item assignment")

    def keys(self) -> KeysView:
        return self.wrapped_dict.keys()
