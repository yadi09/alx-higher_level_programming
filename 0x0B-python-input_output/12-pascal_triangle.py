#!/usr/bin/python3
"""
function that returns a list of lists of integers,
representing the Pascal’s triangle of n:
"""


def pascal_triangle(n):
    pacl_trgl = [[1]]
    if n <= 0:
        return []

    for i in range(0, n - 1):
        _sum = 0
        _list = []
        for x in pacl_trgl[i]:
            if _sum == 0:
                _sum = 1
                _list.append(x)
            else:
                _list.append(pre + x)
            pre = x
        else:
            _list.append(x)
            pacl_trgl.extend([_list])
    return pacl_trgl
