#!/usr/bin/python

import os
import sys
import threading
import time
import math

from multiprocessing import Pool

sys.path.append("./benchmark_cython_module")

import benchmark_cython_module

NUM_ITERATIONS = 1000000
NUM_TASKS = 50


def my_function1(in_value, out_value):
    out_value[in_value] = sum([math.sqrt((z * z) + (z * z * math.pi * math.pi)) + in_value
                               for z in xrange(NUM_ITERATIONS)])


def my_function2(in_value):
    return sum([(math.sqrt(z * z) + (z * z * math.pi * math.pi)) + in_value
                for z in xrange(NUM_ITERATIONS)])


if __name__ == '__main__':
    print ("Running: %s" % os.path.basename(__file__))

    results = {}
    jobs = [threading.Thread(target=my_function1, kwargs=dict(in_value=i, out_value=results))
            for i in xrange(NUM_TASKS)]
    start_time = time.time()
    [t.start() for t in jobs]
    [t.join() for t in jobs]
    end_time = time.time()
    execution_time = end_time - start_time

    print ("Execution time(using threading): %f\n" % execution_time)
    # print ("Results: %s\n" % results.values())

    pool = Pool(processes=4)
    start_time = time.time()
    results = [pool.apply_async(my_function2, [p]) for p in xrange(NUM_TASKS)]
    pool.close()
    pool.join()
    end_time = time.time()
    execution_time = end_time - start_time

    print ("Execution time(using multiprocessing.Pool): %f\n" % execution_time)
    # print ("Results: %s\n" % [x.get() for x in results])

    results = {}
    jobs = [threading.Thread(target=benchmark_cython_module.benchmark01_function1,
                             kwargs=dict(in_value=i, out_value=results, num_iters=NUM_ITERATIONS))
            for i in xrange(NUM_TASKS)]
    start_time = time.time()
    [t.start() for t in jobs]
    [t.join() for t in jobs]
    end_time = time.time()
    execution_time = end_time - start_time

    print ("Execution time(using threading and cython module): %f\n" % execution_time)
    # print ("Results: %s\n" % results.values())

    pool = Pool(processes=4)
    start_time = time.time()
    results = [pool.apply_async(benchmark_cython_module.benchmark01_function2, [p, NUM_ITERATIONS])
               for p in xrange(NUM_TASKS)]
    pool.close()
    pool.join()
    end_time = time.time()
    execution_time = end_time - start_time

    print ("Execution time(using multiprocessing.Pool and cython module): %f\n" % execution_time)
    # print ("Results: %s\n" % [x.get() for x in results])
