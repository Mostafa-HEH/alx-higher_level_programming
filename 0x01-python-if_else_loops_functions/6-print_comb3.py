#!/usr/bin/python3
for i in range(10):
    for x in range(10):
        if i == 8 and x == 9:
            print(89);
        else:
            if x > i:
                print("{:d}{:d}".format(i, x), end=", ")
