"""
Write a function that makes a request to some url
using urllib. Return status code and decoded response data in utf-8
Examples:
     >> make_request('https://www.google.com')
     200, 'response data'
"""
import unittest
from typing import Tuple
from unittest import mock
import urllib.request
from unittest.mock import Mock, MagicMock


def make_request(url: str) -> Tuple[int, str]:
    response = urllib.request.urlopen(url)
    return response.status(), response.read().decode()

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


class TestMakeRequest(unittest.TestCase):
    @mock.patch('urllib.request.urlopen')
    def test_make_request(self, mock_urlopen):
        m = MagicMock()
        m.status.return_value = 200
        m.read.return_value = b'data response'

        mock_urlopen.return_value = m

        self.assertEqual(make_request("https://www.google.com"), (200, 'data response'))


