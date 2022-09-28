#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    matrix_row = []
    for row in matrix:
        for num in row:
            matrix_row.append(num * num)
        new_matrix.append(matrix_row)
        matrix_row = []
    return new_matrix
