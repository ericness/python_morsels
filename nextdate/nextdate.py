import functools
from datetime import date, timedelta
from enum import Enum


class Weekday(Enum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6


class NextDate():
    def __init__(self, weekday: Weekday, after_today: bool = False):
        self.weekday = weekday
        self.after_today = after_today
    
    def days_until(self) -> int:
        """Number of days until specified weekday"""
        until = (self.weekday.value - date.today().weekday()) % 7
        return 7 if until == 0 and self.after_today else until
    
    def date(self) -> date:
        """Return date of next specified weekday"""
        until = self.days_until()
        return date.today() + timedelta(days=until)

    def __repr__(self) -> str:
        return f"NextDay(Weekday.{self.weekday.name},after_today={self.after_today})"


def days_until(day: Weekday, after_today: bool = False) -> int:
    """Number of days until specified weekday"""
    until = (day.value - date.today().weekday()) % 7
    return 7 if until == 0 and after_today else until


def next_date(day: Weekday, after_today: bool = False) -> date:
        """Return date of next specified weekday"""
        until = days_until(day, after_today=after_today)
        return date.today() + timedelta(days=until)


next_tuesday = functools.partial(next_date, Weekday.TUESDAY)
days_to_tuesday = functools.partial(days_until, Weekday.TUESDAY)
