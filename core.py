import multiprocessing

# Get the number of CPU cores
num_cores = multiprocessing.cpu_count()
print(f"Number of CPU cores: {num_cores}")