import tempfile
from typing import Union


class make_file:
    def __init__(
        self,
        contents: Union[str, bytes] = None,
        directory: str = None,
        mode: str = None,
        encoding: str = None,
        newline: str = None,
    ):
        self.contents = contents
        self.contents_mode = "w" if isinstance(contents, str) else "wb"
        self.open_args = {
            "dir": directory,
            "encoding": encoding,
            "newline": newline,
        }
        if mode:
            self.open_args["mode"] = mode
        else:
            self.open_args["mode"] = self.contents_mode

    def __enter__(self) -> str:
        self.temp_file = tempfile.NamedTemporaryFile(**self.open_args)
        if self.contents:
            with open(
                self.temp_file.name,
                self.contents_mode,
                encoding=self.open_args.get("encoding"),
                newline=self.open_args.get("newline"),
            ) as f:
                f.write(self.contents)

        return self.temp_file.name

    def __exit__(
        self,
        exc_type: Exception = None,
        exc_value: BaseException = None,
        traceback=None,
    ):
        self.temp_file.close()
