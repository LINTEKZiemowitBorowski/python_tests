#!/usr/bin/python

import threading
import time
import math


class Worker(threading.Thread):

    def run(self):
        result = 0
        for x in xrange(1000000):
            # print("Iteration: %d" % x)
            p = x * math.pi
            result += math.sqrt(x**2 + p**2)

        return result


if __name__ == '__main__':
    jobs = [Worker() for i in xrange(50)]
    [t.start() for t in jobs]
    start_time = time.time()
    [t.join() for t in jobs]
    end_time = time.time()
    execution_time = end_time - start_time
    print ("Execution time: %f\n" % execution_time)