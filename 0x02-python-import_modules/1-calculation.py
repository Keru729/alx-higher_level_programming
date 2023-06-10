#!/usr/bin/python3 

from calculator_1 import add, sub, mul, div 

if __name__ == "__main__": 

c = 10 
d = 5 

print("{:d} + {:d} = {:d}".format(c, d, add(c, d))) print("{:d} - {:d} = {:d}".format(c, d, sub(c, d))) print("{:d} * {:d} = {:d}".format(c, d, mul(c, d))) print("{:d} / {:d} = {:d}".format(c, d, div(c, d)))
