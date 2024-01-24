#!/usr/bin/python3


def roman_to_int(roman_string):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
                  'D': 500, 'M': 1000}
    prev = _sum = 0

    if type(roman_string) is not str and roman_string is None:
        return 0

    for i in roman_string:
        value = roman_dict.get(i)
        if prev >= value:
            _sum = _sum + prev
            prev = value
        elif prev < value and prev != 0:
            _sum = _sum + (value - prev)
            prev = 0
        else:
            prev = value
    if not prev < value:
        _sum = _sum + prev

    return _sum
