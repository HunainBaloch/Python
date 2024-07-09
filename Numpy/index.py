import numpy as np

# Create two matrices
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])

# Matrix multiplication
matrix_product = np.dot(matrix_a, matrix_b)
print("Matrix A:\n", matrix_a)
print("Matrix B:\n", matrix_b)
print("Matrix A * Matrix B:\n", matrix_product)

# Inverse of a matrix
matrix_a_inv = np.linalg.inv(matrix_a)
print("Inverse of Matrix A:\n", matrix_a_inv)

# Determinant of a matrix
matrix_a_det = np.linalg.det(matrix_a)
print("Determinant of Matrix A:", matrix_a_det)
