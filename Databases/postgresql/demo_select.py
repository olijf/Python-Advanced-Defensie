#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2
import sys

con = None

try:
    connection_string = "host='localhost' " \
                        "port='5432' " \
                        "dbname='products' " \
                        "user='postgres' " \
                        "password='postgres'"
    conn = psycopg2.connect(connection_string)

    cur = conn.cursor()

    # sql = """\
    # INSERT INTO public.demo (id, naam, woonplaats)
    # VALUES (6, 'Xxxx', 'XXXX')"""
    # cur.execute(sql)

    sql = """\
    SELECT naam, woonplaats 
    FROM public.demo
    ORDER BY naam ASC"""
    cur.execute(sql)

    # SQL injection
    plaats = 'Overasselt'

    # sql = """\
    # SELECT naam, woonplaats
    # FROM public.demo
    # WHERE woonplaats = '%s'""" % plaats
    #
    # print(sql)
    #
    # cur.execute(sql)

    cur.execute(
        "prepare prepared_sql as "
        "SELECT naam, woonplaats "
        "FROM public.demo "
        "WHERE woonplaats = $1""")

    cur.execute("execute prepared_sql('%s')" % (plaats))

    while True:
        row = cur.fetchone()

        if row == None:
            break

        print("Naam: " + row[0] + "\t\tWoonplaats: " + row[1])

except psycopg2.DatabaseError as e:
    if conn:
        conn.rollback()

    print('Error %s' % e)
    sys.exit(1)

finally:
    if conn:
        conn.close()