"""
Write a function that makes a request to some url
using urllib. Return status code and decoded response data in utf-8
Examples:
     >>> make_request('https://www.google.com')
     200, 'response data'
"""

from typing import Tuple
from unittest.mock import patch
from urllib.request import urlopen


def make_request(url: str) -> Tuple[int, str]:
    with urlopen(url) as response:
        status = response.status
        content = response.read().decode("utf-8")
        return status, content


# print(make_request("https://docs.python.org/3/"))


"""
Write test for make_request function
Use Mock for mocking request with urlopen https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock
Example:
    >>> m = Mock()
    >>> m.method.return_value = 200
    >>> m.method2.return_value = b'some text'
    >>> m.method()
    200
    >>> m.method2()
    b'some text'
"""


@patch(f"{__name__}.urlopen")
def test_make_request(mock_urlopen):
    mock_response = mock_urlopen.return_value.__enter__.return_value

    mock_response.status = 200
    mock_response.read.return_value.decode.return_value = "some text"

    status, content = make_request("http://urlforsureweirdone.pl")
    assert status == 200
    assert content == "some text"
