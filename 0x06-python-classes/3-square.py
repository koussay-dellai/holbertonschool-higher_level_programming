#!/usr/bin/python3
class Square:
    '''defining a sqaure'''
    def __init__(self, size=0):
        '''initialize an instance'''
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")

    def area(self):
        '''defining a public method'''
        return (self.__size ** 2)
