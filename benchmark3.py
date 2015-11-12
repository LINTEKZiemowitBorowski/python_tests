#!/usr/bin/python

import os
import time
import sqlite3


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

            for m_value in values.values():
                cursor.executemany("INSERT OR REPLACE INTO " + self.SQLITE_TABLE_NAME + " VALUES(?,?)",
                                   [(name, value) for name, value in m_value.items()])
            connection.commit()

        except sqlite3.Error, e:
            print("Database error: %s." % str(e))
            if connection is not None:
                connection.rollback()

        finally:
            if connection is not None:
                connection.close()


if __name__ == '__main__':

    # Prepare test data
    num_iter = 500
    num_records = 20

    my_data = {}

    for i in xrange(num_iter):
        my_keys = ['%d %d' % (i, x) for x in xrange(num_records)]
        my_values = ['Record value: %d %d' % (i, x) for x in xrange(num_records)]
        my_data[i] = dict(zip(my_keys, my_values))

    # print ('Data: %s' % str(data))

    # Remove old database file
    try:
        os.remove('my_database')
    except OSError:
        pass

    # Initialize database
    storage = SQLitePersistentValueStorage()
    storage.init_database('my_database')

    start_time = time.time()

    # Insert data into database
    storage.insert_into_database('my_database', my_data)

    # Read data from the database
    retrieved_data = storage.select_from_database('my_database')

    end_time = time.time()

    execution_time = end_time - start_time
    print ("Execution time: %f\n" % execution_time)

    print ('Num retrieved items: %d' % len(retrieved_data.items()))
    # print ('Retrieved data: %s' % str(retrieved_data))

