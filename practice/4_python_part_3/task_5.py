"""
Write a function that makes a request to some url
using urllib. Return status code and decoded response data in utf-8
Examples:
     >>> make_request('https://www.google.com')
     200, 'response data'
"""
from typing import Tuple
from urllib.request import urlopen
from unittest.mock import Mock, patch

urlopen = Mock(urlopen('https://www.google.com'))
url_open_attrs = {'read.return_value':b'some response text'}
urlopen.configure_mock(**url_open_attrs)

# urlopen('https://www.google.com').__enter__().read.return_value = b'some response text'

def make_request(url: str) -> Tuple[int, str]:
    with urlopen(url) as response:
        status = response.status
        body = response.read().decode("utf-8")
        return f"{status}, '{body}'"

# print(make_request('https://www.google.com'))
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


class TestMakeRequest:


    def test_with_valid_url(self):
        assert make_request('https://www.google.com') == "200, some response text"
# print(urlopen.read().decode())