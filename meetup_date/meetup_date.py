import datetime


def meetup_date(year: int, month: int) -> datetime.date:
    thursday_of_month = 0
    day_of_month = 1
    current_date = None

    while thursday_of_month < 4:
        current_date = datetime.date(year, month, day_of_month)
        if current_date.weekday() == 3:
            thursday_of_month += 1
        day_of_month += 1

    return current_date
