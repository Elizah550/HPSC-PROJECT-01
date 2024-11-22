import numpy as np
import time

# Initialize the profiler using time module
n = 10000  # Decide the length of the vectors
a = np.random.rand(n, 1)  # Create a random column vector a
b = np.random.rand(n, 1)  # Create a random column vector b

# Dot product using matrix multiplication (vectorized operation)
start_time = time.time()
c = np.dot(a.T, b)  # Transpose a and multiply with b
timevec = time.time() - start_time

# Display the result
print("Dot product result:")
print(c)
print(f"Time taken: {timevec:.6f} seconds")
