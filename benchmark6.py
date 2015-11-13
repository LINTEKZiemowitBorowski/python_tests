#!/usr/bin/python

import time
import copy

my_list = [[54, 26, 93, 17, 77, 31, 44, 55, 20],
           [54, 26, 93, 17, 77, 31, 44, 55, 20],
           [54, 26, 93, 17, 77, 31, 44, 55, 20],
           [54, 26, 93, 17, 77, 31, 44, 55, 20],
           [54, 26, 93, 17, 77, 31, 44, 55, 20],
           [54, 26, 93, 17, 77, 31, 44, 55, 20],
           [54, 26, 93, 17, 77, 31, 44, 55, 20],
           [54, 26, 93, 17, 77, 31, 44, 55, 20],
           [54, 26, 93, 17, 77, 31, 44, 55, 20],
           [54, 26, 93, 17, 77, 31, 44, 55, 20]]


def bubble_sort(data_list):
    for pass_num in xrange(len(data_list)-1, 0, -1):
        for i in xrange(pass_num):
            if data_list[i] > data_list[i+1]:
                data_list[i], data_list[i+1] = data_list[i+1], data_list[i]

if __name__ == '__main__':
    # print ("Not sorted data: %s" % my_list)

    start_time = time.time()

    tmp_list = [(copy.deepcopy(my_list)) for x in xrange(10000)]

    copy_time = time.time()

    for sub_list in tmp_list:
        for element in sub_list:
            bubble_sort(element)

    end_time = time.time()

    print ("Copying time: %f" % (copy_time - start_time))
    print ("Sorting time: %f" % (end_time - copy_time))
    # print ("Sorted data: %s" % my_list)