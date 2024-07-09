import numpy as np

# Create a 1D array
array_1d = np.array([1, 2, 3, 4, 5])
print("1D array:", array_1d)

# Create a 2D array
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D array:\n", array_2d)

# Perform basic operations
print("Sum of elements in array_1d:", np.sum(array_1d))
print("Mean of elements in array_2d:", np.mean(array_2d))

# Element-wise operations
array_1d_squared = np.square(array_1d)
print("Squared 1D array:", array_1d_squared)
