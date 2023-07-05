class first:

    # constructor
    def __init__(self):
        # class second object
        # is created
        self.fst = second()

    def first_method(self):
        print("Inside first method")

# define class second


class second:

    # constructor
    def __init__(self):
        self.snd = "GFG"

    def second_method(self):
        print("Inside second method")


# make object of first class
obj1 = first()
print(obj1)

# make object of second class
# with the help of first
obj2 = obj1.fst
print(obj2)

# access attributes and methods
# of second class
print(obj2.snd)

obj2.second_method()

# This code is contributed
# by Deepanshu Rustagi.
