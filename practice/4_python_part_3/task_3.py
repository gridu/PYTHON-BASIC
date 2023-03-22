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
import re
import pytest

def is_http_domain(domain: str) -> bool:
    pattern = r"^((http|https):\/\/)(([\w]-?)+\w\.\w+)(([\w]-?)+\w\.\w+)?\/?$"
    return bool(re.match(pattern, domain))

"""
write tests for is_http_domain function
"""


class TestHTTPDomain:
    def test_valid_domain_http(self):
        assert is_http_domain('http://wikipedia.org')
    
    def test_valid_domain_https(self):
        assert is_http_domain('https://ru.wikipedia.org/')
    
    def test_invalid_domain(self):
        assert not is_http_domain('griddynamics.com')
