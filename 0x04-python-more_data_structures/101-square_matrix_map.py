#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda arg: list(map(lambda num: num ** 2, arg)), matrix))
