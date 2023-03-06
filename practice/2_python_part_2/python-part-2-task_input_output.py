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

def get_input(text):
    return input(text)

def read_numbers(n: int) -> str:
    i = 0
    numbers = []
    while i < n:
        try:
            number = int(get_input("Enter number: "))
            numbers.append(number)
            i += 1
        except:
            i += 1
            continue
    sum = 0
    if len(numbers) == 0:
        print("No numbers entered")
    else:
        for j in numbers:
            sum += j
        average = sum/(len(numbers))
        print("Avg: ", average)
    return numbers

read_numbers(4)