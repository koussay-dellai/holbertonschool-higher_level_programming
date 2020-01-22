#!/usr/bin/python

"""
module to read and print the content of a file
"""


def read_file(filename=""):
    """
    Function to print on stdout
    """
    with open(filename, encoding='UTF8') as f:
        print(f.read(), end="")
