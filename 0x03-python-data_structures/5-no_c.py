#!/usr/bin/env python3
def no_c(my_string):
    modefied_string = [x for x in my_string if not(x == "c" or x == "C")]
    return ("".join(modefied_string))
