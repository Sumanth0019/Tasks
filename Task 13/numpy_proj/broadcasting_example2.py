import numpy as np

# Example 1
a = np.array([1, 2, 3])
b = 10

print("Scalar Broadcasting:", a + b)

# Example 2
a = np.array([[1], [2], [3]])
b = np.array([10, 20, 30])

print("Matrix Broadcasting:\n", a + b)

x = np.random.rand(3, 4)
bias = np.array([1, 2, 3, 4])

print("NN Broadcasting:\n", x + bias)