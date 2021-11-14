from typing import List


def format_fixed_width(
    rows: List[List[str]], padding: int = 2, widths: List[int] = None
) -> str:
    """Format rows of strings as fixed width columns"""
    if widths:
        column_widths = [width + padding for width in widths]
    else:
        column_widths = [max(map(len, elements)) + padding for elements in zip(*rows)]
    result = ""
    for row in rows:
        for index in range(len(row)):
            result += row[index].ljust(column_widths[index])
        result = result.rstrip()
        result += "\n"

    return result.rstrip()
