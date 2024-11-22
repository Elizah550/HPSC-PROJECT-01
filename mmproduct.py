import numpy as np
import time

# Matrix size
n = 10000

# Create random matrix A and vector x
A = np.random.rand(n, n)
x = np.random.rand(n)

# Initialize result vectors
b = np.zeros(n)
bb = np.zeros(n)

# Matrix-vector product using double for-loop
start_time_loop = time.time()
for i in range(n):
    for j in range(n):
        b[i] += A[i, j] * x[j]
end_time_loop = time.time()
timeloop = end_time_loop - start_time_loop
print(f"Time (double for-loop): {timeloop:.6f} seconds")

# Matrix-vector product using single for-loop (vectorized row access)
start_time_loopvec = time.time()
for i in range(n):
    bb[i] = np.dot(A[i, :], x)  # Vectorized row access
end_time_loopvec = time.time()
timeloopvec = end_time_loopvec - start_time_loopvec
print(f"Time (single for-loop with vectorized row): {timeloopvec:.6f} seconds")

# Fully vectorized matrix-vector multiplication
start_time_vec = time.time()
bbb = np.dot(A, x)
end_time_vec = time.time()
timevec = end_time_vec - start_time_vec
print(f"Time (fully vectorized): {timevec:.6f} seconds")

# Compare the results
print(f"Difference between b and bb: {np.linalg.norm(b - bb):.6e}")
print(f"Difference between b and bbb: {np.linalg.norm(b - bbb):.6e}")

# Measure the speed-up
speedup = timeloop / timeloopvec
speedup2 = timeloop / timevec
speedup3 = timeloopvec / timevec

print(f"Speed-up (for-loop vs single for-loop with vectorized row): {speedup:.2f}x")
print(f"Speed-up (for-loop vs fully vectorized): {speedup2:.2f}x")
print(f"Speed-up (single for-loop with vectorized row vs fully vectorized): {speedup3:.2f}x")
