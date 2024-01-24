#!/usr/bin/python3


def weight_average(my_list=[]):
    if my_list == []:
        return 0

    _sum = 0
    mul = 1
    div = 0

    for tup in my_list:
        div = div + tup[-1]
        for val in tup:
            mul = mul * val
        _sum = _sum + mul
        mul = 1

    return _sum/div
