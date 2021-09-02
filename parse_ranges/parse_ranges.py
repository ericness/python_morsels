from typing import Generator, List


def parse_ranges(ranges: str) -> Generator:
    """Create list of numbers in specified ranges"""
    split_ranges = [range.strip() for range in ranges.split(",")]
    for rng in split_ranges:
        start, end = (int(val) for val in rng.split("-"))
        for val in range(start, end + 1):
            yield val
