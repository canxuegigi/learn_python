#!/usr/bin/evn python
#encoding=utf-8
#Author:canxue


import pymysql
import cx_Oracle

def get_mysql_conn():
    #conn = pymysql.connect(host='10.20.2.35', port=3306, user='dba_ops', passwd='FDjkf4O(iSF', db='dba_ops',charset='utf8')
    conn = pymysql.connect(host='127.0.0.1', port=3307, user='root', passwd='', db='dba_ops',charset='utf8')
    return conn

def get_kxods_conn():
    conn = cx_Oracle.connect('ops_kxuser/HOdjf34F95DS@10.30.4.26:1521/odsdb')
    #conn = cx_Oracle.connect('ops_lxuser/Fhjf34F9EDS@10.30.4.36:1521/ods02')
    return conn

def get_lxods_conn():
    conn = cx_Oracle.connect('ops_lxuser/Fhjf34F9EDS@10.30.4.36:1521/ods02')
    return conn

def close_conn(conn):
    conn.close()

def flush_privileges(cursor):
    flush_privileges = 'flush privileges;'
    cursor.execute(flush_privileges)