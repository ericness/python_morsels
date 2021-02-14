import tempfile
from contextlib import contextmanager
from typing import Union


@contextmanager
def make_file(
    contents: Union[str, bytes] = None,
    directory: str = None,
    mode: str = None,
    encoding: str = None,
    newline: str = None,
):
    contents_mode = "w" if isinstance(contents, str) else "wb"
    open_args = {
        "dir": directory,
        "encoding": encoding,
        "newline": newline,
    }
    if mode:
        open_args["mode"] = mode
    else:
        open_args["mode"] = contents_mode

    try:
        temp_file = tempfile.NamedTemporaryFile(**open_args)
        if contents:
            with open(
                temp_file.name,
                contents_mode,
                encoding=open_args.get("encoding"),
                newline=open_args.get("newline"),
            ) as f:
                f.write(contents)

        yield temp_file.name

    finally:
        temp_file.close()
