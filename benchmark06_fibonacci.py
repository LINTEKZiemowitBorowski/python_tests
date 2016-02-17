#!/usr/bin/python

import os
import sys
import time

sys.path.append("./benchmark_cython_module")

import benchmark_cython_module


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == '__main__':
    print ("Running: %s" % os.path.basename(__file__))

    start_time = time.time()
    result0 = fibonacci(40)
    end_time = time.time()
    execution_time = end_time - start_time
    print ("Execution time: %f\n" % execution_time)
    # print ("Result: %d" % result0)

    start_time = time.time()
    result1 = benchmark_cython_module.benchmark06_function(40)
    end_time = time.time()
    execution_time = end_time - start_time
    print ("Execution time (using cython module): %f\n" % execution_time)
    # print ("Result: %d" % result1)