"""
using datetime module find number of days from custom date to now
Custom date is a string with format "2021-12-24"
If entered string pattern does not match, raise a custom Exception
If entered date is from future, return negative value for number of days
    >> calculate_days('2021-10-07')  # for this example today is 6 october 2021
    -1
    >> calculate_days('2021-10-05')
    1
    >>calculate_days('10-07-2021')
    WrongFormatException
"""
from datetime import datetime
from time import strptime
import pytest


class WrongFormatException(Exception):
    pass


def calculate_days(from_date: str) -> int:
    try:
        from_date = datetime.strptime(from_date, "%Y-%m-%d")
        today_date = datetime.now()
        return (today_date - from_date).days
    except ValueError:
        raise WrongFormatException


"""
Write tests for calculate_days function
Note that all tests should pass regardless of the day test was run
Tip: for mocking datetime.now() use https://pypi.org/project/pytest-freezegun/
"""


@pytest.mark.freeze_time('2022-08-30')
def test_past_date():
    assert calculate_days('2022-08-29') == 1
    assert calculate_days('2021-08-30') == 365


@pytest.mark.freeze_time('2022-08-30')
def test_future_date():
    assert calculate_days('2022-09-02') == -3
    assert calculate_days('2024-08-30') == -731


@pytest.mark.freeze_time('2022-08-30')
def test_date_in_wrong_format():
    with pytest.raises(WrongFormatException):
        calculate_days('31-08-2022')

