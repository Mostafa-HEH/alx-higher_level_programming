#!/usr/bin/python3
"""This module divides all elements of a matrix.

Todo:
    * Write a function that divides all elements of a matrix.
"""

def matrix_divided(matrix, div):
    """
    divides all elements of a matrix.
    """
    new_matrix = []
    sub_list = []
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    length = len(matrix[0])
    for ls in matrix:
        if length != len(ls):
            raise TypeError("Each row of the matrix must have the same size")
        for num in ls:
            if not isinstance(num, int) and not isinstance(num, float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            sub_list.append(round(num / div, 2))
        new_matrix.append(sub_list) 
        sub_list = []
    return new_matrix
