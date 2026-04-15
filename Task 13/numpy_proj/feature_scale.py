import numpy as np

x = np.array(([1, 200], [2, 300]))

mean = x.mean(axis=0)
std = x.std(axis=0)

x_scaled = (x - mean) / std

print("Original:\n", x)
print("Mean:", mean)
print("Std:", std)
print("Scaled:\n", x_scaled)