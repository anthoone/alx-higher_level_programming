#!/usr/bin/python3
if __name__ == "__main__":
    def square_matrix_simple(matrix=[]):
        return [[element ** 2 for element in row] for row in matrix]