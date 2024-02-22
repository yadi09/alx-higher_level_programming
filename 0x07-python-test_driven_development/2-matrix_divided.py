#!/usr/bin/python3
"""function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """divides all elements of a matrix by div"""
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    for mrx_list in matrix:
        if type(mrx_list) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for x in mrx_list:
            if type(x) is not int and type(x) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for mrx_list in matrix:
        if len(mrx_list) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    return [[round(x / div, 2) for x in matrix[i]] for i in range(len(matrix))]
