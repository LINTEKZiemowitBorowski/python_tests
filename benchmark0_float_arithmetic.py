#!/usr/bin/python

import os
import threading
import time


class Worker(threading.Thread):

    def run(self):
        result = 0
        for x in xrange(1000000):
            # print("Iteration: %d" % x)
            p = x * 3.14
            result += ((x*x) + (p*p)) / 5.5

        return result


if __name__ == '__main__':
    print ("Running: %s" % os.path.basename(__file__))

    jobs = [Worker() for i in xrange(50)]
    [t.start() for t in jobs]
    start_time = time.time()
    [t.join() for t in jobs]
    end_time = time.time()
    execution_time = end_time - start_time

    print ("Execution time: %f\n" % execution_time)