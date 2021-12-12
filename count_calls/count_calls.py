

class count_calls:
    def __init__(self) -> None:
        self.calls = 0
    
    def __call__(self) -> None:
        self.calls += 1
