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
import pytest
from freezegun import freeze_time
from task import calculate_days, WrongFormatException

@freeze_time("2021-10-06")
def test_calculate_days_past_date():
    result = calculate_days('2021-10-07')
    assert result == -1

@freeze_time("2021-10-06")
def test_calculate_days_future_date():
    result = calculate_days('2021-10-05')
    assert result == 1

@freeze_time("2021-10-06")
def test_calculate_days_wrong_format():
    with pytest.raises(WrongFormatException, match="Wrong date format"):
        calculate_days('10-07-2021')

"""
Write tests for calculate_days function
Note that all tests should pass regardless of the day test was run
Tip: for mocking datetime.now() use https://pypi.org/project/pytest-freezegun/
"""
