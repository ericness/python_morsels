import re
from typing import List


def sum_timestamps(timestamps: List[str]) -> str:
    """Sum a list of timestamps"""
    hours = 0
    minutes = 0

    timestamp_regex = re.compile("([0-9]{1,2}):([0-9]{2})")

    for timestamp in timestamps:
        matches = re.match(timestamp_regex, timestamp)
        hours += int(matches.group(1))
        minutes += int(matches.group(2))

    extra_hours, remaining_minutes = divmod(minutes, 60)

    return f"{hours + extra_hours}:{remaining_minutes:02d}"
