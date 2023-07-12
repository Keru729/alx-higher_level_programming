#!/usr/bin/python3
"""Pascal's Triangle module"""


def pascal_triangle(n):
    """Function that returns a list of
    lists of integers representing the
    Pascal’s triangle of n
    """

    if m <= 0:
        return []

    triangle = [[1]]

    for m in range(1, m):
        row = [1]
        for y in range(1, m):
            row.append(triangle[x-1][y-1] + triangle[x-1][y])
        row.append(1)
        triangle.append(row)
    return triangle
