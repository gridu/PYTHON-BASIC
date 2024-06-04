"""
Write a function that makes a request to some url
using urllib. Return status code and decoded response data in utf-8
Examples:
     >>> make_request('https://www.google.com')
     200, 'response data'
"""
from typing import Tuple
import urllib.request
from unittest.mock import patch, Mock


def make_request(url: str) -> Tuple[int, str]:
    response = urllib.request.urlopen(url)
    return (response.status, response.read())


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


def test_make_request():
    with patch('urllib.request.urlopen') as m:
        m.return_value = Mock()
        m.return_value.status = 200
        m.return_value.read.return_value = b'some text'
        code, response = make_request('https://www.google.com')
        assert code == 200
        assert response == b'some text'
