#!/usr/bin/env python3
def no_c(my_string):
    modefied_string = [x for x in my_string if x != "c" and x != "C"]
    return ("".join(modefied_string))
