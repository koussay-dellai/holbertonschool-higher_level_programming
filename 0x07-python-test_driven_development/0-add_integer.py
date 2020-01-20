#!/usr/bin/python3
"""
   This module contains a fucntion that adds two integers
   and returns an integer number
   typecaste the result
"""
def add_integer(a, b=98):
    """
    Function to add two numbers
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    res = a + b
    if res < 0:
        res = -res
    if res == float("inf"):
        raise ValueError("float overflow")
    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
