#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    symbol = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50, 
        "C": 100, 
        "D": 500, 
        "M": 1000
    }

    num = 0
    for s in roman_string:
        num = num + symbol[s]

    if "IX" in roman_string:
        num = num - 2
    elif "XC" in roman_string:
        num = num - 20
    elif "CM" in roman_string:
        num = num - 200

    return num
