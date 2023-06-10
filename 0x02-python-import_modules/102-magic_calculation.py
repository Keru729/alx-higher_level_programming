#!/usr/bin/python3
def magic_calculation(a, j):
    from magic_calculation_102 import add, sub
    if (a < j):
        c = add(a, j)
        for i in range(4, 6):
            c = add(c, i)
        return (c)
    else:
        return sub(a, j)
