import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import root_scalar
import time

# Define the function
def f(x):
    return np.sin(3 * np.pi * np.cos(2 * np.pi * x) * np.sin(np.pi * x))

# Organizing Inputs
a = -3
b = 5
n = 4**11
x0 = np.linspace(a, b, n)  # Vector containing initial starting points
q = []  # List to store roots

# Finding roots
start_time = time.time()

for i in range(n - 1):
    if np.sign(f(x0[i])) != np.sign(f(x0[i+1])):  # Check if function crosses zero between x0[i] and x0[i+1]
        try:
            sol = root_scalar(f, bracket=[x0[i], x0[i+1]], method='brentq')  # Find roots using Brent's method
            if sol.converged:
                q.append(sol.root)
        except ValueError:
            continue

end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")

# Processing outputs
q = np.unique(np.round(q, decimals=10))  # Keep unique roots only, with tolerance for precision

# Plot the function and roots
xx = np.linspace(a, b, 1001)
plt.figure(figsize=(12, 6))  # Increase the height of the figure
plt.plot(xx, f(xx), '-k', linewidth=2)
plt.plot(q, np.zeros_like(q), 'ro', markerfacecolor='r')  # Plot roots at y=0
plt.xlim([a, b])
plt.ylim([-1.1, 1.1])  # Increase the y-axis limits
plt.yticks([-1, 0, 1])
plt.xlabel('x')
plt.ylabel('f(x)')
plt.gca().set_aspect(3)  # Decrease the aspect ratio to make the plot more stretched
plt.show()
#========================================OLD-CODE=================================
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.optimize import root_scalar
# import time

# # Define the function
# def f(x):
#     return np.sin(3 * np.pi * np.cos(2 * np.pi * x) * np.sin(np.pi * x))

# # Organizing Inputs
# a = -3
# b = 5
# n = 4**11
# x0 = np.linspace(a, b, n)  # Vector containing initial starting points
# q = []  # List to store roots

# # Finding roots
# start_time = time.time()

# for i in range(n - 1):
#     if np.sign(f(x0[i])) != np.sign(f(x0[i+1])):  # Check if function crosses zero between x0[i] and x0[i+1]
#         try:
#             sol = root_scalar(f, bracket=[x0[i], x0[i+1]], method='brentq')  # Find roots using Brent's method
#             if sol.converged:
#                 q.append(sol.root)
#         except ValueError:
#             continue

# end_time = time.time()
# print(f"Time taken: {end_time - start_time} seconds")

# # Processing outputs
# q = np.unique(np.round(q, decimals=10))  # Keep unique roots only, with tolerance for precision

# # Plot the function and roots
# xx = np.linspace(a, b, 1001)
# plt.figure(figsize=(12, 3))
# plt.plot(xx, f(xx), '-k', linewidth=2)
# plt.plot(q, f(q), 'ro', markerfacecolor='r')
# plt.xlim([a, b])
# plt.ylim([-1, 1])
# plt.yticks([-1, 0, 1])
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.gca().set_aspect(4)
# plt.show()
