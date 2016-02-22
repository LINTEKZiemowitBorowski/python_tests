#!/usr/bin/python

import os
import sys
import time
import functools32

sys.path.append("./benchmark_cython_module")

import benchmark_cython_module


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


@functools32.lru_cache(maxsize=128)
def fibonacci_cached(n):
    if n <= 1:
        return n
    return fibonacci_cached(n - 1) + fibonacci_cached(n - 2)


if __name__ == '__main__':
    print ("Running: %s" % os.path.basename(__file__))

    start_time = time.time()
    result0 = fibonacci(40)
    end_time = time.time()
    execution_time = end_time - start_time
    print ("Execution time: %f\n" % execution_time)
    # print ("Result: %d\n" % result0)

    start_time = time.time()
    result1 = fibonacci_cached(40)
    end_time = time.time()
    execution_time = end_time - start_time
    print ("Execution time (using lru_cache): %f\n" % execution_time)
    # print ("Result: %s\n" % result1)

    start_time = time.time()
    result2 = benchmark_cython_module.benchmark06_function(40)
    end_time = time.time()
    execution_time = end_time - start_time
    print ("Execution time (using cython module): %f\n" % execution_time)
    # print ("Result: %d\n" % result2)

    start_time = time.time()
    result3 = benchmark_cython_module.benchmark06_cached_function(40)
    end_time = time.time()
    execution_time = end_time - start_time
    print ("Execution time (using cache and cython module): %f\n" % execution_time)
    # print ("Result: %d\n" % result3)