#!/usr/bin/python3
"""
module to return the number of lines
"""


def number_of_lines(filename=""):
    """
    function to return number of lines
    """
    line_number = 0
    with open(filename, encoding='UTF8') as f:
        for line in f:
            line_number += 1
    return line_number
