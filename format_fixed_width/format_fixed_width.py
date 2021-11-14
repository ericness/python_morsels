import copy
from typing import List


def format_fixed_width(
    rows: List[List[str]],
    padding: int = 2,
    widths: List[int] = None,
    alignments: List[str] = None,
) -> str:
    """Format rows of strings as fixed width columns"""
    if widths:
        column_widths = copy.deepcopy(widths)
    else:
        column_widths = [max(map(len, elements)) for elements in zip(*rows)]

    result = ""

    for row in rows:
        for index in range(len(row)):
            if alignments and alignments[index] == "R":
                result += row[index].rjust(column_widths[index])
            else:
                result += row[index].ljust(column_widths[index])
            result += " " * padding
        result = result.rstrip()
        result += "\n"

    return result.rstrip()
