import numpy as np
import time

# Decide the length of the vectors
n = 10000

# Create random column vectors a and b
a = np.random.rand(n)
b = np.random.rand(n)

# Dot product using a for-loop
c = 0  # Initialize result
start_time_loop = time.time()
for i in range(n):
    c += a[i] * b[i]
end_time_loop = time.time()
timeloop = end_time_loop - start_time_loop
print("Dot product (for-loop):", c)
print("Time (for-loop):", timeloop)

# Dot product using vectorization
start_time_vec = time.time()
cc = np.dot(a, b)  # Vectorized dot product
end_time_vec = time.time()
timevec = end_time_vec - start_time_vec
print("Dot product (vectorized):", cc)
print("Time (vectorized):", timevec)

# Compare the results
difference = abs(c - cc)  # Correct comparison, since c and cc are scalars
print("Difference between the two results:", difference)

# Measure the speed-up
speedup = timeloop / timevec
print("Speed-up:", speedup)
