"""
Write a function that makes a request to some url
using urllib. Return status code and decoded response data in utf-8
Examples:
     # >>> make_request('https://www.google.com')
     200, 'response data'
"""
from typing import Tuple
import requests
from unittest.mock import Mock, patch


def make_request(url: str) -> Tuple[int, str]:
    response = requests.get(url)
    response.encoding = 'utf-8'
    return response.status_code, response.text


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


if __name__ == '__main__':
    requests = Mock()
    response = Mock()
    response1 = Mock()
    requests.get.return_value = response
    response.text = 'Some data'
    response.status_code = 200
    assert make_request('some.url') == (200, 'Some data')
    response1.text = 'Page not found'
    response1.status_code = 404
    requests.get.return_value = response1
    assert make_request('some.url') == (404, 'Page not found')
