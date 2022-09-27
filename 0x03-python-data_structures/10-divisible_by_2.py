#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    is_multiples = []
    for x in my_list:
        if x % 2 == 0:
            is_multiples.append(True)
        else:
            is_multiples.append(False)
    return is_multiples
