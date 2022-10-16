'''
Write a function that accepts a square matrix (N x N 2D array)
and returns the determinant of the matrix.
'''

def determinant(matrix):
    n = len(matrix)

    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for i in range(n):
        minor = [[] for s in range(n-1)]
        for j in range(1, n):
            for k in range(n):
                if k != i:
                    minor[j-1].append(matrix[j][k])
        det += (-1)**i * matrix[0][i] * determinant(minor)

    return det
