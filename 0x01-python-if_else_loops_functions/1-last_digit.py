#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = int(repr(number)[-1])
to_print = "Last digit of {:d} is {:d}".format(number, last_digit)
if last_digit > 5:
    print(to_print + " and is greater than 5")
elif last_digit == 0:
    print(to_print + " and is 0")
elif last_digit < 6 and last_digit != 0:
    print(to_print + " and is less than 6 and not 0")
