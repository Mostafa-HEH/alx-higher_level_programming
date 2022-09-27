#!/usr/bin/python3
def max_integer(my_list=[]):
    biggest = my_list[0]
    if len(my_list) == 0:
        return None
    for x in range(len(my_list)):
        if my_list[x] > biggest:
            biggest = my_list[x]
    return biggest
