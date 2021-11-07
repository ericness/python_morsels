from __future__ import annotations
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
        self._area_code = matches.group(1)
        self._prefix = matches.group(2)
        self._line_number = matches.group(3)

    @property
    def area_code(self) -> str:
        return self._area_code

    @property
    def prefix(self) -> str:
        return self._prefix

    @property
    def line_number(self) -> str:
        return self._line_number

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.area_code}{self.prefix}{self.line_number}')"

    def __str__(self) -> str:
        return f"{self.area_code}-{self.prefix}-{self.line_number}"

    def __eq__(self, other: PhoneNumber) -> bool:
        if not isinstance(other, PhoneNumber):
            return False
        return self.area_code == other.area_code and self.prefix == other.prefix and self.line_number == other.line_number
