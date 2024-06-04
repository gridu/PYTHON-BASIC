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
from datetime import datetime
import pytest
import re


class WrongFormatException(Exception):
    pass


def calculate_days(from_date: str) -> int:
    match = re.match(r'(\d{4})-(\d{2})-(\d{2})', from_date)
    if match == None:
        raise WrongFormatException
    year = int(match.group(1))
    month = int(match.group(2))
    day = int(match.group(3))
    timedelta = datetime.now() - datetime(year, month, day)
    return timedelta.days


"""
Write tests for calculate_days function
Note that all tests should pass regardless of the day test was run
Tip: for mocking datetime.now() use https://pypi.org/project/pytest-freezegun/
"""


@pytest.mark.parametrize('test_input,test_output', [
    ('2021-10-07', -1),
    ('2021-10-05', 1)
])
@pytest.mark.freeze_time('2021-10-06')
def test_correct_format(freezer, test_input, test_output):
    assert calculate_days(test_input) == test_output


@pytest.mark.parametrize('test_input', [
    'test',
    '01-02-2024'
])
def test_wrong_format(test_input):
    with pytest.raises(WrongFormatException):
        calculate_days(test_input)
