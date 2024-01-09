"""
Write a function which detects if entered string is http/https domain name with optional slash at the and
Restriction: use re module
Note that address may have several domain levels
    >>>is_http_domain('http://wikipedia.org')
    True
    >>>is_http_domain('https://ru.wikipedia.org/')
    True
    >>>is_http_domain('griddynamics.com')
    False
"""
import pytest
from task import is_http_domain

def test_is_http_domain_http():
    assert is_http_domain('http://wikipedia.org')

def test_is_http_domain_https():
    assert is_http_domain('https://ru.wikipedia.org/')

def test_is_http_domain_no_http():
    assert not is_http_domain('griddynamics.com')

def test_is_http_domain_with_slash():
    assert is_http_domain('http://example.com/')

def test_is_http_domain_invalid_format():
    assert not is_http_domain('invalid.domain')

"""
write tests for is_http_domain function
"""