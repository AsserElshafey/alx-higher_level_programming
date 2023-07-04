#!/usr/bin/python3
"""defines function to scalar divde matrix"""


def matrix_divided(matrix, div):
    """divides matrix by scalar integer, rounded to two decimal places"""
    if not isinstance(matrix, list) or not matrix:
    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if not isinstance(row, list) or not row:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for element in row:
      if not isinstance(element, (int, float)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            new_element = round(element / div, 2)
            new_row.append(new_element)
        new_matrix.append(new_row)

    return new_matrix
