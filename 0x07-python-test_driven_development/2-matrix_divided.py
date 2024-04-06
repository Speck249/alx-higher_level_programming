#!/usr/bin/python3
"""
Module implements function that divides
each matrix element by divider value.
"""


def matrix_divided(matrix, div):
    """
    Function divides matrix by given number
    and returns output.

    Args:
        matrix: list of lists of integers/floats.
        div: divider of integer/float type.

    Raises:
        TypeError: matrix must be list of lists of integer/float type.
        TypeError: length of nested lists must be equal.
        TypeError: div must be integer or float type not equal to zero.

    Returns:
        New matrix with new values after division.
    """

    if type(matrix) is not list:
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    for element in matrix:
        if not isinstance(element, list):
            raise TypeError('matrix must be a matrix (list of lists) of integers/floats')

    length = len(matrix[0])
    idx = 1
    while idx < len(matrix):
        if len(matrix[idx]) != length:
            raise('Each row of the matrix must have the same size')
        idx += 1

    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    new_matrix = matrix[:]
    for idx in range(len(new_matrix)):
        new_matrix[idx] = [round((num / div), 2) for num in new_matrix[idx]]
    return new_matrix
