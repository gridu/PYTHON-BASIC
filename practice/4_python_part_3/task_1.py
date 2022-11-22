"""
using datetime module find number of days from custom date to now
Custom date is a string with format "2021-12-24"
If entered string pattern does not match, raise a custom Exception
If entered date is from future, return negative value for number of days
    # >>> calculate_days('10-07-2021')
    # WrongFormatException
    >>> calculate_days('2022-11-22')  # for this example today is 21 November 2022
    -1
    >>> calculate_days('2022-11-20')
    1

"""
from datetime import datetime
import pytest


class WrongFormatException(Exception):
    def __init__(self, message='Format is not correct, type: YYYY-MM-DD'):
        self.message = message
        super().__init__(self.message)


def calculate_days(from_date: str) -> int:
    try:
        return (datetime.now() - datetime.fromisoformat(from_date)).days
    except ValueError:
        raise WrongFormatException  # To pass the 3rd test replace it with print(WrongFormatException)


"""
Write tests for calculate_days function
Note that all tests should pass regardless of the day test was run
Tip: for mocking datetime.now() use https://pypi.org/project/pytest-freezegun/
"""


@pytest.fixture
def current_date():
    return datetime.now()


@pytest.mark.freeze_time
def test_calculate_days(current_date, freezer):
    freezer.move_to('2010-10-10')
    assert calculate_days('2010-10-11') == -1
    assert calculate_days('2010-10-09') == 1
    assert calculate_days('2010-10-15') == 5
    with pytest.raises(WrongFormatException):
        calculate_days('11-11-2222')
        calculate_days('baba')


if __name__ == '__main__':
    test_calculate_days()
