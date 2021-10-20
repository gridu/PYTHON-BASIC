Write a function which divides x by y.

If `y == 0` it should print "Division by 0" and return `None`
elif `y == 1` it should raise custom Exception with "Deletion on 1 get the same result" text
else it should return the result of division.

In all cases it should print "Division finished".

```
import typing


def division(x: int, y: int) -> typing.Union[None, int]:
    ...
```

Examples:
```
    >>> division(1, 0)
    Division by 0
    Division finished
    
    >>> division(1, 1)
    Division finished
    DivisionByOneException("Deletion on 1 get the same result")
    
    >>> division(2, 2)
    1
    Division finished
```

Write tests for `division()` function.
- In case (1,1) it should check if exception were raised.
- In case (1,0) it should check if return value is None and "Division by 0" printed.
- If other cases it should check if division is correct.

TIP: to test output of `print()` function use capfd fixture [hint](https://stackoverflow.com/a/20507769).

```
def test_division_ok(capfd):
    ...


def test_division_by_zero(capfd):
    ...


def test_division_by_one(capfd):
    ...
```