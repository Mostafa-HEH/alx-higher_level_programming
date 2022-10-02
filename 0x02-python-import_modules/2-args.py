#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    arg_len = len(argv) - 1
    argument = 'argument' if arg_len == 1 else 'arguments'
    argument += '.' if arg_len == 0 else ':'
    print("{:d} {:s}".format(arg_len, argument))
    if len(argv) > 0:
        for ar in range(1,len(argv)):
            print("{:d}: {}".format(ar, argv[ar]))
