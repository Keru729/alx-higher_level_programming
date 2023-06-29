#!/usr/bin/python3
def add_integer(c, d=98):
    if not isinstance(c, int) and not isinstance(c, float):
        raise TypeError("c must be an integer")
    if not isinstance(d, int) and not isinstance(d, float):
        raise TypeError("d must be an integer")
    if isinstance(c, float):
        c = int(c)
    if isinstance(d, float):
        d = int(d)
    return (c + d)
