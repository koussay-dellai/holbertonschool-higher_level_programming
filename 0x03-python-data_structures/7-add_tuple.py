#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0:
        missing_tuple_a = (0, 0)
    elif len(tuple_a) == 1:
        missing_tuple_a = (tuple_a[0], 0)
    else:
        missing_tuple_a = tuple_a
    if len(tuple_b) == 0:
        missing_tuple_b = (0, 0)
    elif len(tuple_b) == 1:
        missing_tuple_b = (tuple_b[0], 0)
    else:
        missing_tuple_b = tuple_b
    tuple_c = (missing_tuple_a[0] + missing_tuple_b[0],
               missing_tuple_a[1] + missing_tuple_b[1])
    return tuple_c
