import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq
from multiprocessing import Pool
import time

# Organizing Inputs
def f(x):
    return np.sin(3 * np.pi * np.cos(2 * np.pi * x) * np.sin(np.pi * x))

a = -3
b = 5
n = 4**11
x0 = np.linspace(a, b, n)  # Vector containing initial starting points

# Function to find the root using brentq
def find_root(x):
    # Define a small neighborhood around x to use brentq
    try:
        return brentq(f, x - 1e-5, x + 1e-5)  # Searching in a small interval
    except ValueError:
        return None  # Return None if the method fails

# Start parallel pool and timing
if __name__ == '__main__':
    tic = time.time()

    with Pool() as pool:
        q = pool.map(find_root, x0)

    toc = time.time()

    # Filter out None values and remove duplicates
    q = np.unique([root for root in q if root is not None])  # Use list comprehension to filter None

    print(f'Time elapsed: {toc - tic} seconds')

    # Processing Outputs
    showsavePlot = True
    if showsavePlot:
        xx = np.linspace(a-3, b+3, 1001)
        plt.figure(figsize=(12, 6))  # Increase the height of the figure
        plt.plot(xx, f(xx), '-k', linewidth=1.5)
        plt.plot(q, f(q), 'o', markerfacecolor='red', markersize=6, markeredgecolor='red', markeredgewidth=1.5)  # Increase the marker size and edge width
        plt.xlim([a-3, b+3])
        plt.ylim([-1.2, 1.2])  # Increase the y-axis limits
        plt.yticks([-1, 0, 1])
        plt.xlabel('x', fontsize=16)
        plt.ylabel('f(x)', fontsize=16)
        plt.title('Plot of f(x)', fontsize=18)
        plt.gca().set_aspect(3)  # Decrease the aspect ratio to make the plot more stretched
        plt.grid(True, linestyle='--', alpha=0.7)  # Add gridlines
        plt.tight_layout()  # Adjust the layout to fit the plot
        plt.savefig('MySavedPlot.png')
        plt.show()