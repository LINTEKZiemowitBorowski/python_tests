#!/usr/bin/python

import os
import struct
import time

from PyCRC.CRC16 import CRC16

ARRAY_LEN = 255
NUM_DATA = 10000


def prepare_data():
    return [''.join([struct.pack("B", (v + i) % 255) for v in range(0, ARRAY_LEN)]) for i in range(0, NUM_DATA)]

if __name__ == '__main__':
    print ("Running: %s" % os.path.basename(__file__))

    crc = CRC16()
    data = prepare_data()
    # print ("data: %s\n" % data)

    start_time = time.time()
    check_sums = ['%04X' % crc.calculate(data_item) for data_item in data]
    stop_time = time.time()

    print ("Exectution time: %f" % (stop_time - start_time))
    # print ("check_sums: %s\n" % check_sums)
