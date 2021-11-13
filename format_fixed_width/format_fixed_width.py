from typing import List


def format_fixed_width(rows: List[List[str]]) -> str:
    """Format rows of strings as fixed width columns"""
    padding = 2
    column_widths = [max(map(len, elements)) for elements in zip(*rows)]
    result = ""
    for row in rows:
        for index in range(len(row)):
            result += row[index].ljust(column_widths[index] + padding)
        result = result.rstrip()
        result += "\n"

    return result.rstrip()
