#!/usr/bin/python3
class Square:
    '''square class'''
    def __init__(self, size=0):
        '''initialisation of square instance'''
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
