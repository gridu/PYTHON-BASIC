"""
Write a function that makes a request to some url
using urllib. Return status code and decoded response data in utf-8
Examples:
     >>> make_request('https://www.google.com')
     200, 'response data'
"""
from typing import Tuple
from unittest.mock import Mock, patch
import urllib.request

def make_request(url: str) -> Tuple[int, str]:
    try:
        with urllib.request.urlopen(url) as response:
            status_code = response.getcode()
            data = response.read().decode('utf-8')
            return status_code, data
    except urllib.error.URLError as e:
        return getattr(e, 'code', None), ''


@patch('urllib.request.urlopen')
def test_make_request(mock_urlopen):
    mock_response = Mock()
    mock_response.getcode.return_value = 200
    mock_response.read.return_value = b'some text'
    mock_urlopen.return_value = mock_response

    url = 'https://www.example.com'
    status_code, data = make_request(url)

    assert status_code == 200
    assert data == 'some text'
    mock_urlopen.assert_called_once_with(url)




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
