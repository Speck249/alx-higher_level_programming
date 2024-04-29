#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = matrix[:]
    for idx in range(len(new_matrix)):
        new_matrix[idx] = [num * num for num in matrix[idx]]
    return new_matrix
