"""
Write a function which divides x by y.
If y == 0 it should print "Division by 0" and return None
elif y == 1 it should raise custom Exception with "Dividing by 1 gives the same result" text
else it should return the result of division
In all cases it should print "Division finished"
    >>> division(1, 0)
    Division by 0
    Division finished
    >>> division(1, 1)
    Division finished
    DivisionByOneException("Dividing by 1 gives the same result")
    >>> division(2, 2)
    1
    Division finished
"""
import typing


def division(x: int, y: int) -> typing.Union[None, int]:
    ...
