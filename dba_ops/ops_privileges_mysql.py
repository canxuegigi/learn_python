#!/usr/bin/evn python
#encoding=utf-8
#Author:canxue

import conn_manage
import log_temp

"""
查询用户权限
"""
def get_userprivileges(user_name):
    mysql_conn =  conn_manage.get_mysql_conn()
    mysql_cursor = mysql_conn.cursor()
    get_userprivileges_sql = "select user_name,schema_name,table_name,privilege_type,database_name from user_privileges_info where user_name = %s;"
    #print get_userprivileges_sql
    mysql_cursor.execute(get_userprivileges_sql,(user_name))
    print mysql_cursor.fetchall()

    mysql_cursor.close()
    conn_manage.close_conn(mysql_conn)

"""
授予用户权限
"""
def grant_privileges(schema_table_str,user_name,host,valid_time):
    mysql_conn =  conn_manage.get_mysql_conn()
    mysql_cursor = mysql_conn.cursor()
    schema_table_list = schema_table_str.split(',')
    for schema_table in schema_table_list:
        grant_privileges_sql = "grant select on {schema_table} to '{user_name}'@'{host}';".format(schema_table=schema_table,user_name=user_name,host=host)
        mysql_cursor.execute(grant_privileges_sql)
        insert_privileges_sql = "insert into user_privileges_info(user_name,schema_name,table_name,database_name,valid_time) value(%s,%s,%s,%s,%s)"
        print insert_privileges_sql
        mysql_cursor.execute(insert_privileges_sql, (user_name,schema_table.split('.')[0],schema_table.split('.')[1],'mysqlread',valid_time))
        log_temp.log_write('INFO', 'mysql数据库授予 %s 用户 %s表的查询权限' %(user_name,schema_table))

    conn_manage.flush_privileges(mysql_cursor)
    mysql_cursor.close()
    conn_manage.close_conn(mysql_conn)

def main():

    grant_privileges('xd_business.cust_base_info_t,xd_p2p.p2p_code_info,xd_business.lemon_a6_result_t','zhengjing_lixin360','%',2)
    #get_userprivileges( 'zhengjing_lixin360')

if __name__ == '__main__':
    main()


