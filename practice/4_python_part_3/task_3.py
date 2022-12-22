"""
Write a function which detects if entered string is http/https domain name with optional slash at the and
Restriction: use re module
Note that address may have several domain levels
    is_http_domain('http://wikipedia.org')
    True
    is_http_domain('https://ru.wikipedia.org/')
    True
    is_http_domain('griddynamics.com')
    False
"""
import re


def is_http_domain(domain: str) -> bool:
    if not re.search('\Ahttp://', domain) and not re.search('\Ahttps://', domain):
        return False
    if re.search('\.+', domain):
        return True
    return False


if __name__ == '__main__':
    print(is_http_domain('http://wikipedia.org'))
    print(is_http_domain('https://ru.wikipedia.org/'))
    print(is_http_domain('griddynamics.com'))

"""
write tests for is_http_domain function
"""


def tests():
    assert is_http_domain('https://docs.python.org/3/tutorial/stdlib2.html') == True
    assert is_http_domain('https://gridu.litmos.com/home/dashboard/') == True
    assert is_http_domain('google.com') == False
    assert is_http_domain('http://aaaaa') == False


if __name__ == '__main__':
    tests()
