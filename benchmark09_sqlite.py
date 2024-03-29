#!/usr/bin/python

import os
import time
import sqlite3


DATABASE_NAME = '/tmp/my_database'
NUM_ITER = 500
NUM_RECORDS = 20


class SQLitePersistentValueStorage(object):
    SQLITE_TABLE_NAME = "PERSISTENT_VALUES"

    def __init__(self):
        pass

    def init_database(self, database_name):
        connection = None
        try:
            connection = sqlite3.connect(database_name)
            cursor = connection.cursor()
            cursor.execute(
                "CREATE TABLE IF NOT EXISTS " + self.SQLITE_TABLE_NAME + " (PNAME TEXT PRIMARY KEY, PVALUE TEXT)")
            connection.commit()

        except sqlite3.Error, e:
            print("Database error: %s." % str(e))
            if connection is not None:
                connection.rollback()

        finally:
            if connection is not None:
                connection.close()

    def select_from_database(self, database_name):
        connection = None
        result = {}
        try:
            connection = sqlite3.connect(database_name, detect_types=sqlite3.PARSE_DECLTYPES)
            cursor = connection.cursor()
            cursor.execute("SELECT PNAME, PVALUE FROM " + self.SQLITE_TABLE_NAME)
            for row in cursor:
                result[row[0]] = row[1]

        except sqlite3.Error, e:
            print("Database error: %s." % str(e))

        finally:
            if connection is not None:
                connection.close()

        return result

    def insert_into_database(self, database_name, values):
        connection = None
        try:
            connection = sqlite3.connect(database_name)
            connection.text_factory = str
            cursor = connection.cursor()
            cursor.executemany("INSERT OR REPLACE INTO " + self.SQLITE_TABLE_NAME + " VALUES(?,?)",
                               [(name, value) for name, value in values.items()])
            connection.commit()

        except sqlite3.Error, e:
            print("Database error: %s." % str(e))
            if connection is not None:
                connection.rollback()

        finally:
            if connection is not None:
                connection.close()


if __name__ == '__main__':
    print ("Running: %s" % os.path.basename(__file__))

    # Prepare test my_data
    data = [{'%d %d' % (i, x): 'Record value: %d %d' % (i, x) for x in xrange(NUM_RECORDS)} for i in xrange(NUM_ITER)]
    # print ('Data: %s' % str(my_data))

    # Remove old database file
    try:
        os.remove(DATABASE_NAME)
    except OSError:
        pass

    # Initialize database
    storage = SQLitePersistentValueStorage()
    storage.init_database(DATABASE_NAME)

    start_time = time.time()

    # Insert my_data into database
    [storage.insert_into_database(DATABASE_NAME, data[i]) for i in xrange(NUM_ITER)]

    select_time = time.time()

    # Read my_data from the database
    retrieved_data = storage.select_from_database(DATABASE_NAME)

    end_time = time.time()

    inserting_time = select_time - start_time
    reading_time = end_time - select_time
    print ("Inserting time: %f" % inserting_time)
    print ("Reading time: %f" % reading_time)


    print ('Num retrieved items: %d' % len(retrieved_data.items()))
    # print ('Retrieved my_data: %s' % str(retrieved_data))

