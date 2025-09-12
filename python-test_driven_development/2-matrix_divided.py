#!/usr/bin/python3
"""
Module that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.

    Args:
        matrix: list of lists of integers or floats
        div: number to divide by

    Returns:
        New matrix with all elements divided by div, rounded to 2 places

    Raises:
        TypeError: if matrix is not a list of lists of integers/floats
        TypeError: if rows are not the same size
        TypeError: if div is not a number
        ZeroDivisionError: if div is 0
    """
    error_msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list) or not matrix:
        raise TypeError(error_msg)

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(error_msg)

    for row in matrix:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(error_msg)

    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(element / div, 2) for element in row] for row in matrix]
