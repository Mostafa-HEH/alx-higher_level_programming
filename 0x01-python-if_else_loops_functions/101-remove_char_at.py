#!/usr/bin/python3
def remove_char_at(str, n):
    updated_str = ''
    for ch in range(len(str)):
        if ch != n:
            updated_str += str[ch]
    return updated_str
