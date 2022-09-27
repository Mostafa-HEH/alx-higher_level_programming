#!/usr/bin/python3
def new_in_list(my_list, idx, element):

    modified_list = [x for x in my_list]

    # If idx is negative or out of range, return a copy of the original list
    if (idx < 0) or (idx > (len(my_list) - 1)):
        return my_list

    modified_list[idx] = element
    return modified_list
