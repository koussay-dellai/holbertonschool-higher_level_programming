#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square = lambda x : x * x
    list = []
    for i in matrix:
        list.append(map(square, i))
    return list
