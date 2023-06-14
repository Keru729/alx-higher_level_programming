#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        return sum(c * d for c, d in my_list) / sum(c for c, d in my_list)
    return 
