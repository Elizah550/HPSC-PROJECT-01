import numpy as np
import time

# Matrix size
n = 10000

# Generate random matrix and vectors
A = np.random.rand(n, n)
x = np.random.rand(n, 1)
b = np.zeros((n, 1))
bb = np.zeros((n, 1))

# Explicit loop method
start_time = time.time()
for i in range(n):
    for j in range(n):
        b[i] += A[i, j] * x[j]
timeloop = time.time() - start_time
print(f"Time for nested loop: {timeloop:.4f} seconds")

# Loop with vectorized operation for row-wise multiplication
start_time = time.time()
for i in range(n):
    bb[i] = np.dot(A[i, :], x)
timeloopvec = time.time() - start_time
print(f"Time for row-wise vectorized operation: {timeloopvec:.4f} seconds")

# Fully vectorized matrix-vector multiplication
start_time = time.time()
bbb = np.dot(A, x)
timevec = time.time() - start_time
print(f"Time for fully vectorized operation: {timevec:.4f} seconds")

# Norm calculations to check correctness
norm_b_bb = np.linalg.norm(b - bb)
norm_b_bbb = np.linalg.norm(b - bbb)

print(f"Norm difference between b and bb: {norm_b_bb:.4e}")
print(f"Norm difference between b and bbb: {norm_b_bbb:.4e}")

# Speedups
Speedup = timeloop / timeloopvec
Speedup2 = timeloop / timevec
Speedup3 = timeloopvec / timevec

print(f"Speedup (timeloop / timeloopvec): {Speedup:.2f}")
print(f"Speedup (timeloop / timevec): {Speedup2:.2f}")
print(f"Speedup (timeloopvec / timevec): {Speedup3:.2f}")
