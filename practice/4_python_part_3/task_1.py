"""
using datetime module find number of days from custom date to now
Custom date is a string with format "2021-12-24"
If entered string pattern does not match, raise a custom Exception
If entered date is from future, return negative value for number of days
    #>>> calculate_days('2021-10-07')  # for this example today is 6 october 2021
    -1
    #>>> calculate_days('2021-10-05')
    1
    #>>> calculate_days('10-07-2021')
    WrongFormatException
"""
from datetime import datetime
from datetime import date
import pytest
import pytest_freezegun



def calculate_days(from_date: str) -> int:
    format = '%Y-%m-%d'
    try:
        custom_date = datetime.strptime(from_date, format).date()
    except ValueError:
        return print('WrongFormatException')

    today = date.today()
    difference = today - custom_date
    return difference.days


"""
Write tests for calculate_days function
Note that all tests should pass regardless of the day test was run
Tip: for mocking datetime.now() use https://pypi.org/project/pytest-freezegun/
"""


@pytest.mark.freeze_time('2020-03-23')
def test_calculate_days():
    assert calculate_days('2020-03-25') == -2

@pytest.mark.freeze_time('2020-03-23')
def test_calculate_days():
    assert calculate_days('2020-03-23') == 0

@pytest.mark.freeze_time('2020-03-23')
def test_calculate_days():
    assert calculate_days('2020-03-20') == 3

@pytest.mark.freeze_time('2020-03-23')
def test_calculate_days(capfd):
    calculate_days('25-03-2021')
    out, err = capfd.readouterr()
    assert out == 'WrongFormatException\n'
