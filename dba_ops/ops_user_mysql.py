#!/usr/bin/evn python
#encoding=utf-8
#Author:canxue

import conn_manage
import log_temp

"""
创建用户
"""
def create_user(user_name,host,password,email,qq,job_position,department_name,office_addr,mobile_phone):
    mysql_conn = conn_manage.get_mysql_conn()
    mysql_cursor = mysql_conn.cursor()

    create_sql = "create user %s@%s identified by %s;"
    print create_sql
    mysql_cursor.execute(create_sql,(user_name,host,password))

    log_temp.log_write('INFO','mysql数据库创建 %s 用户' %user_name)

    conn_manage.flush_privileges(mysql_cursor)

    save_user_info="insert into dba_ops.user_info(user_name,host,email,qq,job_position,department_name,office_addr,mobile_phone) value(%s,%s,%s,%s,%s,%s,%s,%s)"
    print save_user_info
    mysql_cursor.execute(save_user_info,(user_name,host,email,qq,job_position,department_name,office_addr,mobile_phone))

    mysql_conn.commit()
    mysql_cursor.close()
    conn_manage.close_conn(mysql_conn)
    log_temp.log_write('INFO','%s 用户信息写入dba_ops.user_info' %user_name)


"""
锁定用户
"""
def lock_user(user_name,host):
    mysql_conn = conn_manage.get_mysql_conn()
    mysql_cursor = mysql_conn.cursor()
    lock_user_sql = "alter user %s@%s account lock;"
    print lock_user_sql
    mysql_cursor.execute(lock_user_sql,(user_name,host))

    log_temp.log_write('INFO', 'mysql数据库锁定 %s 用户' % user_name)

    conn_manage.flush_privileges(mysql_cursor)

    alter_user_lock = "update user_info set is_lock = '1' where user_name=%s and host =%s;"
    print alter_user_lock
    mysql_cursor.execute(alter_user_lock,(user_name,host))

    mysql_conn.commit()
    mysql_cursor.close()
    conn_manage.close_conn(mysql_conn)
    log_temp.log_write('INFO', 'user_info锁定 %s 用户' % user_name)
"""
获取用户信息
"""
def get_userinfo(user_name):
    mysql_conn = conn_manage.get_mysql_conn()
    mysql_cursor = mysql_conn.cursor()
    select_sql="select * from user_info where user_name = %s and database_name = 'mysqlread'"
    print select_sql
    effect_row = mysql_cursor.execute(select_sql,(user_name))
    print mysql_cursor.fetchall()
    mysql_conn.commit()
    mysql_cursor.close()
    conn_manage.close_conn(mysql_conn)

def main():

    create_user('zhengjing_lixin360', '%', 'O1234F(Dak56', 'zhengjing@lixin360.com', '810108981','DBA', '研发中心', '成都', '13693461820')
    #get_userinfo('zhengjing_lixin360')
    #lock_user('zhengjing_lixin360','%')

if __name__ == '__main__':
    main()


