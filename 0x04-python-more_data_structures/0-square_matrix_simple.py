#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    Nmatrix = matrix.copy()
    
    for index in range(len(matrix)):
        Nmatrix[index] = list(map((lambda x : x**2), matrix[index]))
    
    return (Nmatrix)
