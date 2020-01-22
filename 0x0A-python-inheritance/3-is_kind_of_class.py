#!/usr/bin/python3

"""
module to check if an object is an instance of a class
"""


def is_kind_of_class(obj, a_class):
    """
    Function return true if the object is an instance of the class
    otherwise it returns false
    """
    result = isinstance(obj, a_class)
    if result:
        return True
    else:
        return False
