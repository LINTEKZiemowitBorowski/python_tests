#!/usr/bin/python

import os
import threading
import time

from multiprocessing import Pool

NUM_ITERATIONS = 100000
NUM_TASKS = 50

my_list = []


def prepare_data():
    # for c in xrange(0x30, 0x79, 3):
    for c in xrange(0x30, 0x39, 3):
        my_list.append(chr(c) + chr(c+1) + chr(c+2))


def my_function1(index, out_value):
    result = []

    for counter in xrange(0, NUM_ITERATIONS):
        output_item = ''
        for item in my_list:
            output_item += item

        result.append(output_item)

    out_value[index] = result


def my_function2():
    result = []

    for counter in xrange(0, NUM_ITERATIONS):
        output_item = ''
        for item in my_list:
            output_item += item

        result.append(output_item)

    return result


def my_function3(index, out_value):
    result = []
    for counter in xrange(0, NUM_ITERATIONS):
        result.append(''.join(my_list))

    out_value[index] = result


def my_function4():
    result = []
    for counter in xrange(0, NUM_ITERATIONS):
        result.append(''.join(my_list))

    return result


if __name__ == '__main__':
    print ("Running: %s" % os.path.basename(__file__))

    prepare_data()

    results = {}
    jobs = [threading.Thread(target=my_function1, kwargs=dict(index=i, out_value=results))
            for i in xrange(NUM_TASKS)]
    start_time = time.time()
    [t.start() for t in jobs]
    [t.join() for t in jobs]
    end_time = time.time()
    execution_time = end_time - start_time

    print ("Execution time(concatenation using threading): %f\n" % execution_time)
    # print ("Output: %s\n" % results.values())

    pool = Pool(processes=4)
    start_time = time.time()
    results = [pool.apply_async(my_function2) for p in xrange(NUM_TASKS)]
    pool.close()
    pool.join()
    end_time = time.time()
    execution_time = end_time - start_time

    print ("Execution time(concatenation using multiprocessing.Pool): %f\n" % execution_time)
    # print ("Output: %s\n" % [x.get() for x in results])

    results = {}
    jobs = [threading.Thread(target=my_function3, kwargs=dict(index=i, out_value=results))
            for i in xrange(NUM_TASKS)]
    start_time = time.time()
    [t.start() for t in jobs]
    [t.join() for t in jobs]
    end_time = time.time()
    execution_time = end_time - start_time

    print ("Execution time(string joining using threading): %f\n" % execution_time)
    # print ("Output: %s\n" % results.values())

    pool = Pool(processes=4)
    start_time = time.time()
    results = [pool.apply_async(my_function4) for p in xrange(NUM_TASKS)]
    pool.close()
    pool.join()
    end_time = time.time()
    execution_time = end_time - start_time

    print ("Execution time(string joining using multiprocessing.Pool): %f\n" % execution_time)
    # print ("Output: %s\n" % [x.get() for x in results])
