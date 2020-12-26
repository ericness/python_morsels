from dataclasses import dataclass
import os
from pathlib import Path
import shutil
import tempfile


@dataclass
class CdResult:
    """Return class from cd context manager"""

    current: Path
    previous: Path


class cd:
    def __init__(self, path: str = None):
        if path:
            self.path = Path(path)
            self.delete_directory = False
        else:
            self.path = Path(tempfile.mkdtemp())
            self.delete_directory = True

    def __enter__(self) -> CdResult:
        self.current_path = Path.cwd()
        self.path.mkdir(parents=True, exist_ok=True)
        os.chdir(self.path)
        return CdResult(self.path, self.current_path)

    def __exit__(
        self,
        exc_type: Exception = None,
        exc_value: BaseException = None,
        traceback=None,
    ):
        os.chdir(self.current_path)
        if self.delete_directory:
            shutil.rmtree(self.path)

    enter = __enter__
    exit = __exit__
