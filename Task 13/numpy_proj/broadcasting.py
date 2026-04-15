# neural network example
import numpy as np
x = np.random.rand(10, 5)
bias = np.array([1, 2, 3, 4, 5])

output = x + bias  # broadcasting

print("Input shape:", x.shape)
print("Bias shape:", bias.shape)
print("Output:\n", output)