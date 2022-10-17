#!/usr/bin/python3
"""This module prints a text with 2 new lines after each of these: ., ? and :

Todo:
    * prints a text with 2 new lines after each of these: ., ? and :
"""

def text_indentation(text):
    """
    slice with two lines after ., ?, : .
    """
    is_next = False
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in range(0, len(text)):
        if text[i] == ' ':
            is_next = True
        if is_next:
            if text[i] == ' ':
                continue
        print("{:s}".format(text[i]), end="")
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print("")
            print("")
            is_next = True
