#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    arglen = len(argv)
    counter = 0
    if arglen > 0:
        for arg in range(1, arglen):
            counter += int(argv[arg])
    print(counter)
