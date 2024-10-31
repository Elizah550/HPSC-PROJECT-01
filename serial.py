import time
from timeconsumingfun import timeconsumingfun

if __name__ == '__main__':
    n = 100
    start_time = time.time()
    for i in range(n):
        timeconsumingfun(i)

    end_time = time.time()

    exe = end_time - start_time  # Calculate the execution time
    print(f'The execution time is: {exe:.4f} seconds')
