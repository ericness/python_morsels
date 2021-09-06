from typing import Generator, List


def parse_ranges(ranges: str) -> Generator:
    """Create list of numbers in specified ranges"""
    split_ranges = [range.strip() for range in ranges.split(",")]
    for rng in split_ranges:
        split_nums = [int(val) for val in rng.split("-")]
        if len(split_nums) == 2:
            start, end = split_nums[0], split_nums[1]
        else:
            start, end = split_nums[0], split_nums[0]
        for val in range(start, end + 1):
            yield val
