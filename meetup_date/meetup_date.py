import calendar
import datetime


def meetup_date(year: int, month: int, nth: int = 4, weekday: int = 3) -> datetime.date:
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
