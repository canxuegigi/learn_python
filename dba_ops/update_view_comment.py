#!/usr/bin/evn python
#encoding=utf8
#Author:canxue

import conn_manage
import log_temp
import os,sys
#os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

view_list = []
view_col_list = []
view_col_sql = []

def update_view_comment():
    #need_update_view_sql = "select schema,table_name,view_name from ops_user.table_view_info where type = '1' and view_name = 'T_LOAN_BASE_INFO_V_NEW'"
    need_update_view_sql = "select schema,table_name,view_name from ops_user.table_view_info where type = '1'"
    oracle_conn = conn_manage.get_kxods_conn()
    oracle_cursor = oracle_conn.cursor()

    oracle_cursor.execute(need_update_view_sql)

    for row_record in oracle_cursor.fetchall():
        view_list.append([row_record[0],row_record[1],row_record[2]])
        view_col_list.append([row_record[0],row_record[1],row_record[2]])
    oracle_cursor.close()
    conn_manage.close_conn(oracle_conn)
    print view_list

    #获取表备注
    oracle_conn = conn_manage.get_kxods_conn()
    oracle_cursor = oracle_conn.cursor()
    for row in view_list:
        get_tab_comment = "select comments from dba_tab_comments where owner = '{schema}' and table_name = '{table_name}'".format(
            schema=row[0], table_name=row[1])
        oracle_cursor.execute(get_tab_comment)
        for row_record in oracle_cursor.fetchall():
            row.append(row_record[0])
    print view_list

    """"""
    #获取字段备注
    oracle_conn = conn_manage.get_kxods_conn()
    oracle_cursor = oracle_conn.cursor()
    for row in view_col_list:
        get_tab_comment = "select column_name,comments from dba_col_comments where owner = '{schema}' and table_name = '{table_name}'".format(
            schema=row[0], table_name=row[1])
        oracle_cursor.execute(get_tab_comment)
        for row_record in oracle_cursor.fetchall():
            col_sql = "COMMENT ON column {scheme}.{tab}.{col} IS '{comment}';".format(scheme=row[0],tab=row[2],col=row_record[0],comment=row_record[1])
            try:
                col_sql_sql = col_sql.decode('gbk')
            except:
                continue
            print col_sql_sql

    #执行视图备注
    oracle_conn = conn_manage.get_kxods_conn()
    oracle_cursor = oracle_conn.cursor()
    for row in view_list:
        try:
            add_view_com = "COMMENT ON TABLE {scheme}.{tab} IS '{comment}';".format(scheme=row[0],tab=row[2],comment=row[3])
            add_view_com_sql = add_view_com.decode('gbk')
        except:
            continue
        #print add_view_com
        print add_view_com_sql
        #传不了
        #oracle_cursor.execute(add_view_com)

def main():
    update_view_comment()

if __name__ == '__main__':
    main()




