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

def check(input):
    try:
        val=int(input)
        return True
    except ValueError:
         return False

def read_numbers(n: int) -> str:

    i=0
    numbers=[]

    while i < n:
      
       input1=input("Enter number: ")
       if check(input1):
        num=int(input1)
        numbers.append(num)
       i=i+1
       
    
    if len(numbers)==0:
            return "No numbers entered!"
    else:
            a=sum(numbers)/len(numbers)
            return "Avg is: ",a


print(read_numbers(5))