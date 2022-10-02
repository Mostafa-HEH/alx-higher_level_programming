#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_len = len(sys.argv) - 1
    argument = 'argument' if arg_len == 1 else 'arguments'
    argument += '.' if arg_len == 0 else ':'
    print("{:d} {:s}".format(arg_len, argument))
    if len(sys.argv) > 0:
        for ar in range(1,len(sys.argv)):
            print("{:d}: {}".format(ar, sys.argv[ar]))
