#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    bigest_key = ''
    temp = 0
    for k, v in a_dictionary.items():
        if v > temp:
            temp = v
            bigest_key = k
    return bigest_key
