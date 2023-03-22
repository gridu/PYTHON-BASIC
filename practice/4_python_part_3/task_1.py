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
from freezegun import freeze_time
import pytest 

class WrongFormatException(Exception):
    pass

def calculate_days(from_date: str) -> int:
    date_format = '%Y-%m-%d'
    current_date = datetime.strptime(datetime.today().strftime(date_format), date_format)
    try:
        from_date = datetime.strptime(from_date, date_format)
    except ValueError:
        raise WrongFormatException(f"{from_date} format is invalid. Format should match '{date_format}'")
    return abs((current_date - from_date).days)

"""
Write tests for calculate_days function
Note that all tests should pass regardless of the day test was run
Tip: for mocking datetime.now() use https://pypi.org/project/pytest-freezegun/
"""

@freeze_time("2023-03-20")
class TestCalculateDays:
    def test_past_date_correct_format(self):
        assert calculate_days('2023-03-13') == 7
    
    def test_future_date_correct_format(self):
        assert calculate_days('2023-03-30') == 10
    
    def test_date_incorrect_format(self):
        with pytest.raises(WrongFormatException):
            calculate_days('09-20-2022')