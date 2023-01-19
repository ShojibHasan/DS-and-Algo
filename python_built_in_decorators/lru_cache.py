# @lru_cache: Speed Up Your Programs by Caching
'''
This decorator can be used to cache the results of a function, so that subsequent calls to the function with the same arguments will not be executed again.

It is especially helpful for functions that are computationally expensive or that are called frequently with the same arguments.


'''
import time
from functools import lru_cache


def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

start_time = time.perf_counter()
print(fibonacci(30))
end_time = time.perf_counter()
print(f"The execution time: {end_time - start_time:.8f} seconds")


@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


start_time = time.perf_counter()
print(fibonacci(30))
end_time = time.perf_counter()
print(f"The execution time: {end_time - start_time:.8f} seconds")