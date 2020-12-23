import os
from pathlib import Path


class cd:
    def __init__(self, path: str):
        self.path = Path(path)

    def __enter__(self):
        self.current_path = Path.cwd()
        self.path.mkdir(parents=True, exist_ok=True)
        os.chdir(self.path)

    def __exit__(self, exc_type: Exception, exc_value: BaseException, traceback):
        os.chdir(self.current_path)
