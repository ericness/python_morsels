import re
from typing import List


def sum_timestamps(timestamps: List[str]) -> str:
    """Sum a list of timestamps"""
    hours = 0
    minutes = 0
    seconds = 0

    timestamp_regex = re.compile("((?P<hours>[0-9]{1,2}):)?(?P<minutes>[0-9]{1,2}):(?P<seconds>[0-9]{2})")

    for timestamp in timestamps:
        matches = re.match(timestamp_regex, timestamp)
        match_groups = matches.groupdict()
        if match_groups.get("hours"):
            hours += int(matches.group("hours"))
        minutes += int(matches.group("minutes"))
        seconds += int(matches.group("seconds"))

    extra_minutes, remaining_seconds = divmod(seconds, 60)
    minutes += extra_minutes

    extra_hours, remaining_minutes = divmod(minutes, 60)
    hours += extra_hours

    second_str = f"{remaining_seconds:02d}"
    minute_str = (
        f"{remaining_minutes}"
        if remaining_minutes < 10 and hours == 0
        else f"{remaining_minutes:02d}"
    )
    hour_str = f"{hours}" if hours else ""
    return ":".join(part for part in [hour_str, minute_str, second_str] if part)
