import tempfile


class make_file:

    def __enter__(self) -> str:
        self.filename = tempfile.NamedTemporaryFile()
        return self.filename.name

    def __exit__(self,
                 exc_type: Exception = None,
                 exc_value: BaseException = None,
                 traceback=None,
                 ):
        self.filename.close()
