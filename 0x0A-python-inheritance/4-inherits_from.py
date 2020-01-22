#!/usr/bin/python3

"""
module to check wether an object is an instance that that inherited from
the specified class
"""


def inherits_from(obj, a_class):
    """
    Function to return True if an object inherited from a class
    otherwise it returns False
    """
    result = issubclass(type(obj), a_class)
    if result and (type(obj) != a_class):
        return True
    else:
        return False
