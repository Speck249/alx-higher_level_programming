#!/usr/bin/python3
"""
Module implements function that
returns product of two matrices.
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Function accepts two matrices, calculates and
    returns matrix product using numpy.matmul.

    Args:
        m_a: first input array operand.
        m_b: second input array operand.

    Raises:
        TypeError: invalid data type for einsum.
        ValuError: scalar values must not be passed.
                   input matrices must have compatible
                   dimensions

    Returns:
        matrix product of inputs that's only scalar
        if input arrays are 1-d vectors..
    """

    return np.matmul(m_a, m_b)
