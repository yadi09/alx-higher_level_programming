#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):

    if matrix != [[]]:
        for length in range(len(matrix)):
            for i in range(len(matrix[length])):
                if i != (len(matrix[length]) - 1):
                    print("{:d}".format(matrix[length][i]), end=" ")
                else:
                    print("{:d}".format(matrix[length][i]))
    else:
        print()
