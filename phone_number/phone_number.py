import re

PHONE_NUMBER_REGEX = re.compile(r"""
    ^[^a-zA-Z0-9]*
    ([0-9]{3})     # area code
    [^a-zA-Z0-9]*
    ([0-9]{3})     # prefix
    [^a-zA-Z0-9]*
    ([0-9]{4})     # line number
    [^a-zA-Z0-9]*$
""", re.VERBOSE)


class PhoneNumber:
    """Stores a US phone number"""

    def __init__(self, number: str):
        matches = PHONE_NUMBER_REGEX.search(number)
        if not matches:
            raise ValueError('Invalid phone number')
        self.area_code = matches.group(1)
        self.prefix = matches.group(2)
        self.line_number = matches.group(3)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.area_code}{self.prefix}{self.line_number}')"

    def __str__(self) -> str:
        return f"{self.area_code}-{self.prefix}-{self.line_number}"
