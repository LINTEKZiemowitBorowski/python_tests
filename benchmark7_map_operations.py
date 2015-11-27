#!/usr/bin/python

import os
import time
import random

SEQUENCE_LEN = 1000000
MAX_VALUE = 99999999


def get_randoms():
    return [random.randrange(0, MAX_VALUE + 1, 1) for _ in range(SEQUENCE_LEN)]


def build_map(my_keys):
    return {k: "%d" % k for k in my_keys}


def search_map(my_keys, my_map):
    return [int(my_map[key]) for key in my_keys]


if __name__ == '__main__':
    print ("Running: %s" % os.path.basename(__file__))

    # Prepare data
    created_keys = get_randoms()
    print("created_keys len: %d\n" % len(created_keys))
    # print("created_keys: %s\n" % created_keys)

    start_time = time.time()
    random_map = build_map(created_keys)

    # print("Map len: %d\n" % len(random_map))

    build_time = time.time()
    found_values = search_map(created_keys, random_map)
    search_time = time.time()

    print("found_values len: %d\n" % len(found_values))

    if len(created_keys) != len(found_values):
        print("Error, len of created_keys(%d) is different then len of keys found in the map (%d)\n" %
              (len(created_keys), len(found_values)))

    print("Build map time: %f\n" % (build_time - start_time))
    print("Search map time: %f\n" % (search_time - build_time))
