"""
using datetime module find number of days from custom date to now
Custom date is a string with format "2021-12-24"
If entered string pattern does not match, raise a custom Exception
If entered date is from future, return negative value for number of days
    >>> calculate_days('2021-10-07')  # for this example today is 6 october 2021
    -1
    >>> calculate_days('2021-10-05')
    1
    >>> calculate_days('10-07-2021')
    WrongFormatException
"""

import re
from datetime import datetime

import pytest


class WrongFormatException(Exception):
    pass


def calculate_days(from_date: str) -> int:
    date_pattern = r"[1-9][0-9][0-9][0-9]-[01][0-9]-[0-3][0-9]"

    if not re.fullmatch(date_pattern, from_date):
        raise WrongFormatException

    now = datetime.now()
    second_date = datetime.strptime(from_date, "%Y-%m-%d")

    diff = now - second_date
    diff_days = diff.days

    return diff_days


"""
Write tests for calculate_days function
Note that all tests should pass regardless of the day test was run
Tip: for mocking datetime.now() use https://pypi.org/project/pytest-freezegun/
"""


@pytest.mark.freeze_time("2026-06-17")
def test_calculate_days_from_past():
    diff = calculate_days("2026-06-15")
    assert diff == 2


@pytest.mark.freeze_time("2026-06-17")
def test_calculate_days_from_future():
    diff = calculate_days("2026-06-20")
    assert diff == -3


@pytest.mark.freeze_time("2026-06-17")
def test_calculate_days_wrong_format():
    with pytest.raises(WrongFormatException):
        calculate_days("10-07-2021")
