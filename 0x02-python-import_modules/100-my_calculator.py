#!/usr/bin/python3
from sys import argv, exit
from calculator_1 import add, sub, mul, div

if __name__ == '__main__':
    argv.pop(0)
    argvlength = len(argv)

    if (argvlength == 3):
        l = int(argv[0])
        m = int(argv[2])

        if (argv[1] == "+"):
            print("{:d} + {:d} = {:d}".format(l, m, add(l, m)))
        elif (argv[1] == "-"):
            print("{:d} - {:d} = {:d}".format(l, m, sub(l, m)))
        elif (argv[1] == "*"):
            print("{:d} * {:d} = {:d}".format(l, m, mul(l, m)))
        elif (argv[1] == "/"):
            print("{:d} / {:d} = {:d}".format(l, m, div(l, m)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
    else:
        print("Usage: ./100-my_calculator.py <l> <operator> <m>")
        exit(1)
