#!/usr/bin/python

import os
import time
import copy
import random
import numpy
import array

SEQUENCE_LEN = 10000
ITERATIONS = 10
MAX_VALUE = 10000


def bubble_sort(data_list):
    for pass_num in xrange(len(data_list)-1, 0, -1):
        for i in xrange(pass_num):
            if data_list[i] > data_list[i+1]:
                data_list[i], data_list[i+1] = data_list[i+1], data_list[i]


if __name__ == '__main__':
    print ("Running: %s" % os.path.basename(__file__))

    # Prepare data
    my_randoms = [random.randrange(0, MAX_VALUE + 1, 1) for _ in range(SEQUENCE_LEN)]
    # print ("Not sorted data: %s" % my_list)

    # Test loop
    for case in ['A', 'B']:

        start_time = time.time()

        tmp_list = [(copy.deepcopy(my_randoms)) for _ in range(ITERATIONS)]

        copy_time = time.time()

        if case == 'A':
            for sub_list in tmp_list:
                sub_list.sort()
        else:
            for sub_list in tmp_list:
                bubble_sort(sub_list)

        end_time = time.time()

        print ("Python list copying time, case %s: %f" % (case, (copy_time - start_time)))
        print ("Python list sorting time, case %s: %f" % (case, (end_time - copy_time)))
        # print ("Sorted data: %s" % tmp_list)

    for case in ['A', 'B']:

        start_time = time.time()

        tmp_list = [array.array('i', my_randoms) for _ in range(ITERATIONS)]

        copy_time = time.time()

        if case == 'A':
            tmp_list = numpy.sort(tmp_list)
        else:
            for sub_list in tmp_list:
                bubble_sort(sub_list)

        end_time = time.time()

        print ("Python array copying time, case %s: %f" % (case, (copy_time - start_time)))
        print ("Python array soring time, case %s: %f" % (case, (end_time - copy_time)))
        # print ("Sorted data: %s" % tmp_list)

    for case in ['A', 'B']:

        start_time = time.time()

        tmp_list = numpy.array([my_randoms for _ in range(ITERATIONS)])

        copy_time = time.time()

        if case == 'A':
            tmp_list = numpy.sort(tmp_list)
        else:
            for sub_list in tmp_list:
                bubble_sort(sub_list)

        end_time = time.time()

        print ("Numpy copying time, case %s: %f" % (case, (copy_time - start_time)))
        print ("Numpy sorting time, case %s: %f" % (case, (end_time - copy_time)))
        # print ("Sorted data: %s" % tmp_list)
