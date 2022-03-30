"""
Write a function that makes a request to some url
using urllib. Return status code and decoded response data in utf-8
Examples:
     #>>> make_request('https://www.google.com')
     200, 'response data'
"""
from typing import Tuple
from unittest import mock
import urllib.request
import pytest

def make_request(url: str) -> Tuple[int, str]:
    response = urllib.request.urlopen(url)
    response_utf = response.read().decode('utf8')
    code = response.status
    return (code, response_utf)

a, b = make_request('https://google.com')

print('status= ', a, '\n', 'content =', b[:50])


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

@mock.patch('urllib.request.urlopen')
def test_make_request(mock_urlopen):
    mock_urlopen.return_value.status = 200
    mock_urlopen.return_value.read.return_value = 'Some content...'.encode('utf8')

    code, response = make_request('https://foo/')
    assert code == 200
    assert response == 'Some content...'
