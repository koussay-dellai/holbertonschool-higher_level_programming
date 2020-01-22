#!/usr/bin/python3
"""
module to overrite a file
"""


def write_file(filename="", text=""):
    """
    function that writes a string to a text file
    """
    with open(filename, mode='w', encoding='UTF8') as f:
        f.write(text)
    return len(text)
