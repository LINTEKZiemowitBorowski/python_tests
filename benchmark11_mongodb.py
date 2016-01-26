#!/usr/bin/python

import os
import time
import pymongo


DATABASE_NAME = 'my_database'
COLLECTION_NAME = 'my_collection'
NUM_ITER = 500
NUM_RECORDS = 20


def init_database():
    dc = pymongo.MongoClient()[DATABASE_NAME][COLLECTION_NAME]
    dc.delete_many({})
    dc.create_index([("RecordId", pymongo.ASCENDING)])


def insert_into_database(value_set):
    dc = pymongo.MongoClient()[DATABASE_NAME][COLLECTION_NAME]
    for value_item in value_set:
        dc.insert_many(value_item)


def update_into_database(query, value):
    dc = pymongo.MongoClient()[DATABASE_NAME][COLLECTION_NAME]
    return dc.update_many(query, value)


def select_from_database(query):
    dc = pymongo.MongoClient()[DATABASE_NAME][COLLECTION_NAME]
    return dc.find(query, {"_id": False}).sort([("RecordId", pymongo.ASCENDING)])


if __name__ == '__main__':
    print ("Running: %s" % os.path.basename(__file__))

    # Prepare test my_data
    my_data = [[{'RecordId': (100 * i) + x, 'RecordValue': '%d %d' % (i, x)} for x in xrange(NUM_RECORDS)]
               for i in xrange(NUM_ITER)]

    # Initialize database
    init_database()

    t0 = time.time()

    # Insert my_data into database
    insert_into_database(my_data)

    t1 = time.time()

    # Read my_data from the database
    inserted_data = [select_from_database({"RecordId": {"$gte": (i * 100), "$lt": ((i * 100) + 100)}})
                     for i in xrange(NUM_ITER)]

    t2 = time.time()

    # Update my_data in the database
    [update_into_database({"RecordId": {"$gte": (i * 100), "$lt": ((i * 100) + 100)},
                           "RecordValue": {"$regex": ".*0$"}},
                          {"$set": {"RecordValue": "updated"}})
     for i in xrange(NUM_ITER)]

    t3 = time.time()

    # Read my_data from the database again
    updated_data = select_from_database({"RecordValue": "updated"})

    t4 = time.time()

    print ("Inserting time: %f" % (t1 - t0))
    print ("Reading time: %f" % (t2 - t1))
    print ("Updating time: %f" % (t3 - t1))
    print ("Reading time: %f" % (t4 - t3))

    print ('Num inserted items: %d' % sum([inserted_data[i].count() for i in xrange(NUM_ITER)]))
    print ('Num updated items: %d' % updated_data.count())

    # print ('Source data: %s' % str(my_data))
    #
    # print ('Database data:')
    # for subset in inserted_data:
    #     for record in subset:
    #         print record
    #
    # print ('Updated data:')
    # for record in updated_data:
    #         print record




