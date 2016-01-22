#!/usr/bin/python

import os
import time
from pymongo import MongoClient


DATABASE_NAME = 'my_database'
COLLECTION_NAME = 'my_collection'
NUM_ITER = 500
NUM_RECORDS = 20


def init_database():
    dc = MongoClient()[DATABASE_NAME][COLLECTION_NAME].delete_many({})


def insert_into_database(value_set):
    dc = MongoClient()[DATABASE_NAME][COLLECTION_NAME]
    for value_item in value_set:
        dc.insert_many(value_item)


def select_from_database():
    dc = MongoClient()[DATABASE_NAME][COLLECTION_NAME]
    return dc.find({}, {"_id": False})


if __name__ == '__main__':
    print ("Running: %s" % os.path.basename(__file__))

    # Prepare test my_data
    my_data = [[{'%d %d' % (i, x): 'Record value: %d %d' % (i, x)} for x in xrange(NUM_RECORDS)]
               for i in xrange(NUM_ITER)]
    # print ('Data: %s' % str(my_data))

    # Initialize database
    init_database()

    start_time = time.time()

    # Insert my_data into database
    insert_into_database(my_data)

    select_time = time.time()

    # Read my_data from the database
    retrieved_data = select_from_database()

    end_time = time.time()

    inserting_time = select_time - start_time
    reading_time = end_time - select_time
    print ("Inserting time: %f" % inserting_time)
    print ("Reading time: %f" % reading_time)
    print ('Num retrieved items: %d' % retrieved_data.count())

    for record in retrieved_data:
        print record




