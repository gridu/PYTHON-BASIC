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


def is_http_domain(domain: str) -> bool:
    pattern = r"^https?://.+\.[a-zA-Z]+/?$"
    if re.match(pattern, domain):
        return True
    return False


"""
write tests for is_http_domain function
"""


def test_is_http_domain_http():
    assert is_http_domain("http://wikipedia.org")


def test_is_http_domain_https():
    assert is_http_domain("https://ru.wikipedia.org/")


def test_is_http_domain_no_http():
    assert not is_http_domain("griddynamics.com")


def test_is_http_domain_dot_at_the_end():
    assert not is_http_domain("https://ru.wikipedia.")
