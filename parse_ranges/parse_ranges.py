from typing import List


def parse_ranges(ranges: str) -> List:
    """Create list of numbers in specified ranges"""
    result = []
    split_ranges = [range.strip() for range in ranges.split(",")]
    for rng in split_ranges:
        start, end = (int(val) for val in rng.split("-"))
        result.extend(range(start, end + 1))
    return result
