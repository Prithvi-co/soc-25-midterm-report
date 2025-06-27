 import numpy as np

# Create a 4x2 array of random integers
matrix = np.random.randint(50, 150, size=(4, 2))
print("Matrix:\n", matrix)

# Shape and dtype
print("Shape of matrix:", matrix.shape)
print("Data type of matrix:", matrix.dtype)

# Basic operations
print("Max value:", matrix.max())
print("Min value:", matrix.min())
print("Standard Deviation:", matrix.std())
print("Transposed Matrix:\n", matrix.T)

# Broadcasting example with different shapes
x = np.array([[5], [10], [15]])
y = np.array([2, 4, 6])
# To make broadcasting work, adjust y to shape (1, 3)
y = y.reshape(1, 3)

# Now add x (3x1) to y (1x3) to get a (3x3) result
print("Broadcasted Addition Result:\n", x + y)
