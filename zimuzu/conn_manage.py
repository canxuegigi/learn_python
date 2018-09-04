#!/usr/bin/evn python
#encoding=utf-8
#Author:canxue

import pymysql

def get_mysql_conn():
    conn = pymysql.connect(host='127.0.0.1', port=3307, user='spider', passwd='spider', db='spider',charset='utf8')
    return conn

def close_conn(conn):
    conn.close()