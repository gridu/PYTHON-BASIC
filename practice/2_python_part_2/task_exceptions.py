"""
Write a function which divides x by y.
If y == 0 it should print "Division by 0" and return None
elif y == 1 it should raise custom Exception with "Deletion on 1 get the same result" text
else it should return the result of division
In all cases it should print "Division finished"
    >>> division(1, 0)
    Division by 0
    Division finished
    >>> division(1, 1)
    Division finished
    DivisionByOneException("Deletion on 1 get the same result")
    >>> division(2, 2)
    1
    Division finished
"""
import typing

def division(x: int, y: int) -> typing.Union[None, int]:
    stmt = "Division finished"
    if y == 0:
        print("Division by 0")
        print(stmt)
        return None
    elif y == 1:
        print(stmt)
        raise Exception("Division by 1 returns the same result")
    else:
        print(stmt)
        return int(x/y)