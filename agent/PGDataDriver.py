#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: bustta
# @Date:   2015-01-20 23:46:46
# @Last Modified by:   bustta
# @Last Modified time: 2015-01-21 00:42:21

import os
import psycopg2


def open_pg_connection():
    conn = psycopg2.connect(
        database=os.environ['PTTNOTIFIER_DB'],
        user=os.environ['PTTNOTIFIER_DB_DEFAULT_USER'],
        password=os.environ['PTTNOTIFIER_DB_DEFAULT_PASSWORD'],
        host=os.environ['PG_HOST_IP'], port=os.environ['PG_PORT'])
    return conn


def close_pg_connection(pg_conn):
    pg_conn.close()


def get_pg_cursor(pg_conn):
    return pg_conn.cursor()


def execute_and_fetchall(sql, cur):
    cur.execute(sql)
    return cur.fetchall()
