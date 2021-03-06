#!/usr/bin/python3
"""
module to return a new matrix that contains its divided
elements
"""

def matrix_divided(matrix, div):
    """
    Function to return a new matrix
    """
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if type(matrix[i][j]) is not int and type(matrix[i][j]) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            for x in range(len(matrix) - 1):
                if (len(matrix[x]) != len(matrix[x + 1])):
                    raise TypeError("Each row of the matrix must have the same size")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if (div == 0):
        raise ZeroDivisionError("division by zero")
    new_matrix = [[],[]]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            division = round((matrix[i][j] / 3), 2)
            new_matrix[i].append(division)
    return new_matrix
