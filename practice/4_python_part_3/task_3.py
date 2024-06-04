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
    match = re.match(r'^(https?://)[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)+/?$', domain)
    return match is not None


"""
write tests for is_http_domain function
"""


@pytest.mark.parametrize('test_input,test_output', [
    ('http://wikipedia.org', True),
    ('https://ru.wikipedia.org/', True),
    ('griddynamics.com', False),
    ('?????', False),
    ('https://....', False),
    ('http:////////', False)
])
def test_is_http_domain(test_input, test_output):
    assert is_http_domain(test_input) == test_output
