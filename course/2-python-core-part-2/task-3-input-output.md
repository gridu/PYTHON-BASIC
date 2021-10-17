Write function which reads a number from input nth times.

If an entered value isn't a number, ignore it.
After all inputs are entered, calculate an average entered number.

Return string with following format:
If average exists, return: `Avg: X`, where X is avg value which rounded to 2 places after the decimal.
If it doesn't exist, return: `No numbers entered`

```
def read_numbers(n: int) -> str:
    ...
```

Examples:
```
# user enters: 1, 2, hello, 2, world
>>> read_numbers(5)
Avg: 1.67

# user enters: hello, world, foo, bar, baz
>>> read_numbers(5)
No numbers entered
```

Write tests for a `read_numbers` function.
It should check successful and failed cases, for example:
- Test if user inputs: 1, 2, 3, 4
- Test if user inputs: 1, 2, Text

Tip: for passing custom values to the `input()` function use `unittest.mock.patch` function [doc](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch).

```
from unittest.mock import patch


def test_read_numbers_without_text_input():
    ...


def test_read_numbers_with_text_input():
    ...
```