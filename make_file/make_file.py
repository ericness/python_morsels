import tempfile


class make_file:
    def __init__(self, contents: str = None):
        self.contents = contents

    def __enter__(self) -> str:
        self.temp_file = tempfile.NamedTemporaryFile()
        if self.contents:
            with open(self.temp_file.name, "w") as f:
                f.write(self.contents)

        return self.temp_file.name

    def __exit__(self,
                 exc_type: Exception = None,
                 exc_value: BaseException = None,
                 traceback=None,
                 ):
        self.temp_file.close()
