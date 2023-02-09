"""
Write a function that makes a request to some url
using urllib. Return status code and decoded response data in utf-8
Examples:
     >>> make_request('https://www.google.com')
     200, 'response data'
"""
from typing import Tuple
from urllib.request import urlopen
from urllib.error import HTTPError
import ssl

def make_request(url: str) -> Tuple[int, str]:
    ssl._create_default_https_context = ssl._create_unverified_context
    try:
        with urlopen(url) as response:
            status_code = response.getcode()
            response_data = response.read().decode('utf-8')
            return status_code, response_data
    except HTTPError as e:
        return e.getcode(), e.read().decode('utf-8')
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
