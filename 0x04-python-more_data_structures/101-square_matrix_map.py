#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda u: list(map(lambda z: z**2, u)), matrix))
