#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for idx in range(len(matrix)):
        for items in matrix[idx]:
            print('{}'.format(items), end=' ')
        print()
