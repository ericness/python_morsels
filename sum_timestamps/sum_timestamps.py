import re
from typing import List


def sum_timestamps(timestamps: List[str]) -> str:
    """Sum a list of timestamps"""
    hours = 0
    minutes = 0
    seconds = 0

    timestamp_regex = re.compile("([0-9]{1,2}):([0-9]{2})")

    for timestamp in timestamps:
        matches = re.match(timestamp_regex, timestamp)
        minutes += int(matches.group(1))
        seconds += int(matches.group(2))

    extra_minutes, remaining_seconds = divmod(seconds, 60)
    minutes += extra_minutes

    hours, remaining_minutes = divmod(minutes, 60)

    second_str = f"{remaining_seconds:02d}"
    minute_str = (
        f"{remaining_minutes}"
        if remaining_minutes < 10 and hours == 0
        else f"{remaining_minutes:02d}"
    )
    hour_str = f"{hours}" if hours else ""
    return ":".join(part for part in [hour_str, minute_str, second_str] if part)
