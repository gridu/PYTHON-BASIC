"""
Write a function which detects if entered string is http/https domain name with optional slash at the and
Restriction: use re module
Note that address may have several domain levels
    #>>>is_http_domain('http://wikipedia.org')
    True
    #>>>is_http_domain('https://ru.wikipedia.org/')
    True
    #>>>is_http_domain('griddynamics.com')
    False
"""
import re
import pytest

def is_http_domain(domain):
    pattern = re.compile(r'(https?://)?(www\.)?(\w+)?(\w+)(\.\w+/?)')
    matches = pattern.finditer(domain)
    for match in matches:
        if match.group(1) == None:
            return False
        else:
            return True


"""
write tests for is_http_domain function
"""

scenarios = [
    ('http://ru.something.net', True),
    ('ru.something.net/', False),
    ('https://ru.something.net', True),
    ('httpgh://ru.something.net', False),
    ('something.com', False),
    ('blablablablabla', None),
]

@pytest.mark.parametrize('url, result', scenarios)
def test_is_http_domain(url, result):
    assert is_http_domain(url) == result
