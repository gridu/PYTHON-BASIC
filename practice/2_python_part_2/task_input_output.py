"""
Write function which reads a number from input nth times.
If an entered value isn't a number, ignore it.
After all inputs are entered, calculate an average entered number.
Return string with following format:
If average exists, return: "Avg: X", where X is avg value which rounded to 2 places after the decimal
If it doesn't exists, return: "No numbers entered"
Examples:
    user enters: 1, 2, hello, 2, world
    >>> read_numbers(5)
    Avg: 1.67
    ------------
    user enters: hello, world, foo, bar, baz
    >>> read_numbers(5)
    No numbers entered

"""

def read_numbers(n: int) -> str:
    total = 0
    count = 0

    for _ in range(n):
        try:
            value = float(input("Enter a number: "))
            total += value
            count += 1
        except ValueError:
            pass  # Ignore non-numeric input

    if count > 0:
        average = total / count
        return f"Avg: {average:.2f}\n{'-' * 12}"
    else:
        return "No numbers entered"


# Test case
result = read_numbers(5)
print(result)


