#!/usr/bin/python

import time


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == '__main__':
    start_time = time.time()
    fibonacci(40)
    end_time = time.time()
    execution_time = end_time - start_time
    print ("Execution time: %f\n" % execution_time)