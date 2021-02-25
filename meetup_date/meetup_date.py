import calendar
import datetime
from enum import IntEnum
from typing import Union


class Weekday(IntEnum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6


def meetup_date(
    year: int, month: int, nth: int = 4, weekday: Union[int, Weekday] = 3
) -> datetime.date:
    nth_counter = 0
    if nth > 0:
        day_of_month = 1
        increment = 1
    else:
        _, day_of_month = calendar.monthrange(year, month)
        increment = -1
    current_date = None

    while nth_counter < abs(nth):
        current_date = datetime.date(year, month, day_of_month)
        if current_date.weekday() == weekday:
            nth_counter += 1
        day_of_month += increment

    return current_date
