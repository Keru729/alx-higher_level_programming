#!/usr/bin/python3
# 8-uppercase.py
# Kerubel Solomon <kibi729@gmail.com>

def uppercase(str):
    
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            c = chr(ord(c) - 32)
        print("{}".format(c), end="")
    print("")
