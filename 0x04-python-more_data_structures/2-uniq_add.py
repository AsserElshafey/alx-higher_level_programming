#!/usr/bin/python3
def uniq_add(my_list=[]):
    Sum = 0
    for x in set(my_list):
        Sum += x
    return Sum
