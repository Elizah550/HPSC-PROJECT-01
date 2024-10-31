import multiprocessing
import time
from timeconsumingfun import timeconsumingfun

if __name__ == '__main__':
    n = 100
    with multiprocessing.Pool(processes=8) as pool:
        start_time = time.time()
        pool.map(timeconsumingfun, range(n))
        end_time = time.time()

    exe = end_time - start_time
    print(f'The execution time is tp: {exe:.4f}')