"""
Write a function which detects if entered string is http/https domain name with optional slash at the end
Restriction: use re module
Note that address may have several domain levels
    >>> is_http_domain('http://wikipedia.org')
    True
    >>> is_http_domain('https://ru.wikipedia.org/')
    True
    >>> is_http_domain('griddynamics.com')
    False
"""
import re


def is_http_domain(domain: str) -> bool:
    is_http = re.match("(^https?:\/\/).*(\..{1,6}\/?$)", domain)
    return bool(is_http)


"""
write tests for is_http_domain function
"""


def test_http_domain():
    assert is_http_domain("http://abcd.co.uk") is True
    assert is_http_domain("http://qwerty.com") is True


def test_https_domain():
    assert is_http_domain("https://dcba.oc.ku") is True
    assert is_http_domain("https://ytrewq.moc") is True


def test_wrong_domains():
    assert is_http_domain("grlddynamlcs.com") is False
    assert is_http_domain("dynamlcsgrld.co.uk/") is False
    assert is_http_domain("http.com") is False
    assert is_http_domain("https.cc/") is False


def test_slash_at_the_end():
    assert is_http_domain("http://abcd.gov.cc/") is True
    assert is_http_domain("https://qwerty.com/") is True
    assert is_http_domain("https:/abcd.coc/") is False
