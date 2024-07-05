#!/usr/bin/python3
"function find_peak"


def find_peak(list_of_integers):
    "finds a peak"
    li = list_of_integers
    lng = len(li)
    if lng == 0:
        return
    m = lng // 2
    if (m == lng - 1 or li[m] >= li[m + 1]) and (m == 0 or li[m] >= li[m - 1]):
        return li[m]
    if m != lng - 1 and li[m + 1] > li[m]:
        return find_peak(li[m + 1:])
    return find_peak(li[:m])
