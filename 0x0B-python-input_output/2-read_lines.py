#!/usr/bin/python3
"""
module to print lines of a file
"""


def read_lines(filename="", nb_lines=0):
    """
    function to print n lines of a file
    """
    number = 0
    with open(filename, encoding="UTF8") as f:
        for i in f:
            number += 1
        if (nb_lines <= 0) or (nb_lines >= number):
            print(f.read(), end="")
        else:
            for x in range(nb_lines):
                print(f.readline(), end="")
