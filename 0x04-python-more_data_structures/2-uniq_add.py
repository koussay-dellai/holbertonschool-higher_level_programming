#!/usr/bin/python3
def uniq_add(my_list=[]):
    s1 = set(my_list)
    j = 0
    for i in s1:
        j += i
    return j
