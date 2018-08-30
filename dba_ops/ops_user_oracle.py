#!/usr/bin/evn python
#encoding=utf-8
#Author:canxue

import conn_manage
import log_temp

"""
创建用户
"""
def create_user(user_name,database_name,password,email,qq,job_position,department_name,office_addr,mobile_phone):
    """oracle创建用户"""
    if str.lower(database_name) == 'lxods':
        oracle_conn = conn_manage.get_lxods_conn()
        oracle_cursor = oracle_conn.cursor()
    elif str.lower(database_name) == 'kxods':
        oracle_conn = conn_manage.get_kxods_conn()
        oracle_cursor = oracle_conn.cursor()
    else:
        exit()

    create_sql = "create user {user_name} identified by {password}".format(user_name=user_name,password=password)
    print create_sql
    oracle_cursor.execute(create_sql)

    create_session_sql = "grant create session to {user_name} ".format(user_name=user_name)
    print create_session_sql
    oracle_cursor.execute(create_session_sql)

    oracle_conn.commit()
    oracle_cursor.close()
    conn_manage.close_conn(oracle_conn)

    log_temp.log_write('INFO','oracle数据库创建 %s 用户' %user_name)


    """向mysql写入数据"""
    mysql_conn = conn_manage.get_mysql_conn()
    mysql_cursor = mysql_conn.cursor()
    save_user_info="insert into dba_ops.user_info(user_name,database_name,email,qq,job_position,department_name,office_addr,mobile_phone) value(%s,%s,%s,%s,%s,%s,%s,%s)"
    print save_user_info
    mysql_cursor.execute(save_user_info,(user_name,database_name,email,qq,job_position,department_name,office_addr,mobile_phone))

    mysql_conn.commit()
    mysql_cursor.close()
    conn_manage.close_conn(mysql_conn)

    log_temp.log_write('INFO','%s 用户信息写入 dba_ops.user_info' %user_name)

"""
锁定用户
"""
def lock_user(user_name,database_name):
    if str.lower(database_name) == 'lxods':
        oracle_conn = conn_manage.get_lxods_conn()
        oracle_cursor = oracle_conn.cursor()
    elif str.lower(database_name) == 'kxods':
        oracle_conn = conn_manage.get_kxods_conn()
        oracle_cursor = oracle_conn.cursor()
    else:
        exit()

    lock_user_sql = "alter user {user_name} account lock".format(user_name=user_name)
    print lock_user_sql
    oracle_cursor.execute(lock_user_sql)
    oracle_conn.commit()
    oracle_cursor.close()
    conn_manage.close_conn(oracle_conn)

    log_temp.log_write('INFO', 'oracle数据库锁定 %s 用户' % user_name)

    mysql_conn = conn_manage.get_mysql_conn()
    mysql_cursor = mysql_conn.cursor()
    alter_user_lock = "update user_info set is_lock = '1' where user_name='{user_name}' and database_name = '{database_name}'".format(user_name=user_name,database_name=database_name)
    print alter_user_lock
    mysql_cursor.execute(alter_user_lock)
    mysql_conn.commit()
    mysql_cursor.close()
    conn_manage.close_conn(mysql_conn)

    log_temp.log_write('INFO', 'user_info表锁定 %s 用户' % user_name)

"""
获取用户信息
"""
def get_userinfo(user_name):
    mysql_conn = conn_manage.get_mysql_conn()
    mysql_cursor = mysql_conn.cursor()
    select_sql="select * from user_info where user_name = '{user_name}'".format(user_name=user_name)
    print select_sql
    effect_row = mysql_cursor.execute(select_sql)
    print mysql_cursor.fetchall()
    mysql_conn.commit()
    mysql_cursor.close()
    conn_manage.close_conn(mysql_conn)

def main():
    #create_user('zhengjing_lixin360','lxods', 'h1234HS56', 'zhengjing@lixin360.com','810108981', 'DBA', '研发中心', '成都', '13693461820')
    #create_user('zhengjing_lixin360','kxods', 'h1234HS56', 'zhengjing@lixin360.com','810108981', 'DBA', '研发中心', '成都', '13693461820')
    #get_userinfo('zhengjing_lixin360')
    #lock_user('zhengjing_lixin360','kxods')

if __name__ == '__main__':
    main()




