#!/usr/bin/python3
"""
Module implements function that
returns product of two matrices.
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Function accepts two matrices, calculates and
    returns product with dot notation multiplication.

    Args:
        m_a: first matrix operand.
        m_b: second matrix operand.

    Raises:
        TypeError: matrix must be list of lists.
                   matrices must contain int or float values.
                   matrices must have compatible dimensions.
        ValueError: neither matrices must be empty.

    Returns:
        Product of two matrices.
    """

    if type(m_a) is not list and type(m_b) is not list:
        raise TypeError('matrix must be a list')

    for val in m_a:
        if len(val) == 0:
            raise ValueError('matrix must not be empty')

    for val in m_b:
        if len(val) == 0:
            raise ValueError('matrix must not be empty')

    for val in m_a:
        if type(val) is not list:
            raise TypeError('matrix must be list of lists')

    for val in m_b:
        if type(val) is not list:
            raise TypeError('matrix must be list of lists')

    m_a_dimension = np.array(m_a)
    m_b_dimension = np.array(m_b)

    if m_a_dimension.shape[1] != m_b_dimension.shape[0]:
        raise TypeError('matrices must have compatible dimensions')

    for val in m_a:
        for num in val:
            if type(num) is not int and type(num) is not float:
                raise TypeError('matrix lists must contain int or float')

    for val in m_b:
        for num in val:
            if type(num) is not int and type(num) is not float:
                raise TypeError('matrix lists must contain int or float')

    return (np.dot(m_a, m_b)).tolist()
