# -*- coding:utf8 -*-
import pymysql

# Connect to the databases

connection = pymysql.connect(host = 'docker.testing-studio.com',
                             user = 'hogwarts',
                             password = 'hogwarts',
                             db = 'seveniruby',
                             )

try:
    # with connection.cursor() as cursor:
    #     # Create a new record
    #     sql = "select * from departments"
    #     cursor.execute(sql, ('sds@163.com', 'very-secret'))
    #
    # # connection is not autocommit by default. So you must commit to save
    # # your changes.
    #
    # connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "select * from departments"
        cursor.execute(sql)
        result = cursor.fetchmany()
        print(result)
finally:
    connection.close()
