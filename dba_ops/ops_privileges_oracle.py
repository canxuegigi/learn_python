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
授予用户对象权限
"""
def grant_obj_privileges(schema_table_str,user_name,database_name,valid_time):
    if str.lower(database_name) == 'lxods':
        oracle_conn = conn_manage.get_lxods_conn()
        oracle_cursor = oracle_conn.cursor()
    elif str.lower(database_name) == 'kxods':
        oracle_conn = conn_manage.get_kxods_conn()
        oracle_cursor = oracle_conn.cursor()
    else:
        exit()

    mysql_conn =  conn_manage.get_mysql_conn()
    mysql_cursor = mysql_conn.cursor()

    schema_table_list = schema_table_str.split(',')
    for schema_table in schema_table_list:
        grant_privileges_sql = "grant select on {schema_table} to {user_name}".format(schema_table=schema_table,user_name=user_name)
        oracle_cursor.execute(grant_privileges_sql)

        insert_privileges_sql = "insert into user_privileges_info(user_name,schema_name,table_name,database_name,valid_time) value(%s,%s,%s,%s,%s)"
        print insert_privileges_sql
        mysql_cursor.execute(insert_privileges_sql, (user_name,schema_table.split('.')[0],schema_table.split('.')[1],database_name,valid_time))
        log_temp.log_write('INFO', 'oracle数据库授予 %s 用户 %s表的查询权限' %(user_name,schema_table))

    conn_manage.flush_privileges(mysql_cursor)

    oracle_cursor.close()
    conn_manage.close_conn(oracle_conn)
    mysql_conn.commit()
    mysql_cursor.close()
    conn_manage.close_conn(mysql_conn)


def main():
    #grant_obj_privileges('SR_KX_SN.SNTBL_BUS_APPLY,PCLODS.S_NPLM_YOOLI_LOAN_PHASE','zhengjing_lixin360','kxods',2)
    #grant_obj_privileges('sr_lx_bs.crf_p2p_refuse_code_info,sr_lk_cust.t_staff_whitelist','zhengjing_lixin360','lxods',1)
    get_userprivileges( 'zhengjing_lixin360')

if __name__ == '__main__':
    main()


