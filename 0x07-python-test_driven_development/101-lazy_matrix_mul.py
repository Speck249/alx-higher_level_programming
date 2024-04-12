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
        m_a: first matrix
        m_b: second matrix

    Raises:
        TypeError: matrices must be list of lists.
                   matrices must contain int or float elements.
                   matrices must have compatible dimensions.

    Returns:
        Product of two matrices.
    """

    if type(m_a) is not list and type(m_b) is not list:
        raise TypeError('matrix must be of type list')

    for val in m_a:
        if type(val) is not list:
            raise TypeError('matrix must be list of lists')

    for val in m_b:
        if type(val) is not list:
            raise TypeError('matrix must be list of lists')

    for val in m_a:
        for num in val:
            if type(num) is not int and type(num) is not float:
                raise TypeError('matrix lists must contain int or float.')

    for val in m_b:
        for num in val:
            if type(num) is not int and type(num) is not float:
                raise TypeError('matrix lists must contain int or float.')

    m_a_dimension = np.array(m_a)
    m_b_dimension = np.array(m_b)

    if m_a_dimension.shape[1] != m_b_dimension.shape[0]:
        raise TypeError('matrices must have compatible dimensions')

    return np.dot(m_a, m_b)
