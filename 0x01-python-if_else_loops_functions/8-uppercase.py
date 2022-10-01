#!/usr/bin/python3
def uppercase(str):
    upper_word = ''
    for ch in str:
        if 96 < ord(ch) < 123:
            upper_word += chr(ord(ch) - 32)
        else:
            upper_word += ch
    print(upper_word)
