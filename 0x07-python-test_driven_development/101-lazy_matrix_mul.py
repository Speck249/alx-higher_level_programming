#!/usr/bin/python3
"""Module presents function that multiplies two matrices."""

import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices using numpy.

    Args:
        m_a: list of lists of integers or floats.
        m_b: list of lists of integers or floats. 

    Returns:
        Product of two matrices.

    """

    m_c = np.dot(m_a, m_b)
    return m_c
