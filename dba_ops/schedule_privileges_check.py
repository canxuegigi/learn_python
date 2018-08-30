#!/usr/bin/evn python
#encoding=utf-8
#Author:canxue

import conn_manage
import log_temp

#存放回收权限相关信息
check_result = []
#存放回收权限相关信息
re_grant_list = []

def privileges_check():
    mysql_conn = conn_manage.get_mysql_conn()
    mysql_cursor = mysql_conn.cursor()
    check_sql = "SELECT upi.user_name,ui.`host`,upi.schema_name,upi.table_name,upi.database_name,upi.auto_id,upi.privilege_type FROM user_privileges_info upi join user_info ui on upi.user_name = ui.user_name and upi.database_name = ui.database_name where upi.valid_time < DATEDIFF(CURRENT_DATE(),upi.create_time) and upi.is_used = 1;"
    print check_sql
    mysql_cursor.execute(check_sql)

    for row_record in mysql_cursor.fetchall():
        if row_record[4] == '10.20.2.35(lxkxreadonly)':
            check_result.append((row_record[5],row_record[4],"REVOKE {privilege_type} on {schema_name}.{table_name} from '{user_name}'@'{host}';".format(privilege_type=row_record[6],schema_name=row_record[2],table_name=row_record[3],user_name=row_record[0],host=row_record[1])))
            re_grant_list.append((row_record[5],row_record[4],"grant {privilege_type} on {schema_name}.{table_name} to '{user_name}'@'{host}';".format(privilege_type=row_record[6],schema_name=row_record[2],table_name=row_record[3],user_name=row_record[0],host=row_record[1])))
        elif row_record[4] == '10.30.4.36(LXODS)':
            check_result.append((row_record[5],row_record[4],"REVOKE {privilege_type} on {schema_name}.{table_name} from {user_name}".format(privilege_type=row_record[6],schema_name=row_record[2],table_name=row_record[3],user_name=row_record[0])))
            re_grant_list.append((row_record[5],row_record[4],"grant {privilege_type} on {schema_name}.{table_name} to {user_name}".format(privilege_type=row_record[6],schema_name=row_record[2],table_name=row_record[3],user_name=row_record[0])))
        elif row_record[4] == '10.30.4.26(KXODS)':
            check_result.append((row_record[5],row_record[4],"REVOKE {privilege_type} on {schema_name}.{table_name} from {user_name}".format(privilege_type=row_record[6],schema_name=row_record[2],table_name=row_record[3],user_name=row_record[0])))
            re_grant_list.append((row_record[5],row_record[4],"grant {privilege_type} on {schema_name}.{table_name} to {user_name}".format(privilege_type=row_record[6],schema_name=row_record[2],table_name=row_record[3],user_name=row_record[0])))
        else:
            pass
    mysql_cursor.close()
    conn_manage.close_conn(mysql_conn)


"""重新给用户授权"""
def re_grant_privileges(re_grant_list):
    mysql_conn = conn_manage.get_mysql_conn()
    mysql_cursor = mysql_conn.cursor()

    lxods_conn = conn_manage.get_lxods_conn()
    lxods_cursor = lxods_conn.cursor()

    kxods_conn = conn_manage.get_lxods_conn()
    kxods_cursor = kxods_conn.cursor()

    for grant_sql in re_grant_list:
        if grant_sql[1] == '10.20.2.35(lxkxreadonly)':
            mysql_cursor.execute(grant_sql[2])

        elif grant_sql[1] == '10.30.4.36(LXODS)':
            lxods_cursor.execute(grant_sql[2])

        elif grant_sql[1] == '10.30.4.26(KXODS)':
            kxods_cursor.execute(grant_sql[2])

    conn_manage.flush_privileges(mysql_cursor)
    mysql_conn.commit()
    mysql_cursor.close()
    conn_manage.close_conn(mysql_conn)

    lxods_conn.commit()
    lxods_cursor.close()
    conn_manage.close_conn(lxods_conn)

    kxods_conn.commit()
    kxods_cursor.close()
    conn_manage.close_conn(kxods_conn)


"""回收用户权限"""
def revoke_privileges(check_result):
    mysql_conn = conn_manage.get_mysql_conn()
    mysql_cursor = mysql_conn.cursor()

    lxods_conn = conn_manage.get_lxods_conn()
    lxods_cursor = lxods_conn.cursor()

    kxods_conn = conn_manage.get_lxods_conn()
    kxods_cursor = kxods_conn.cursor()

    for revoke_sql in check_result:
        if revoke_sql[1] == '10.20.2.35(lxkxreadonly)':
            update_use_sql = "update user_privileges_info set is_used = 0 WHERE auto_id = '{auto_id}'; ".format(auto_id=revoke_sql[0])
            mysql_cursor.execute(revoke_sql[2])
            mysql_cursor.execute(update_use_sql)

        elif revoke_sql[1] == '10.30.4.36(LXODS)':
            update_use_sql = "update user_privileges_info set is_used = 0 WHERE auto_id = '{auto_id}'; ".format(auto_id=revoke_sql[0])
            lxods_cursor.execute(revoke_sql[2])
            mysql_cursor.execute(update_use_sql)

        elif revoke_sql[1] == '10.30.4.26(KXODS)':
            update_use_sql = "update user_privileges_info set is_used = 0 WHERE auto_id = '{auto_id}'; ".format(auto_id=revoke_sql[0])
            kxods_cursor.execute(revoke_sql[2])
            mysql_cursor.execute(update_use_sql)

    conn_manage.flush_privileges(mysql_cursor)
    mysql_conn.commit()
    mysql_cursor.close()
    conn_manage.close_conn(mysql_conn)

    lxods_conn.commit()
    lxods_cursor.close()
    conn_manage.close_conn(lxods_conn)

    kxods_conn.commit()
    kxods_cursor.close()
    conn_manage.close_conn(kxods_conn)


def main():
    privileges_check()
    #重新授权
    #re_grant_privileges(re_grant_list)
    print 'check_result:\n',check_result
    print 're_grant_list:\n',re_grant_list
    #是否调用
    #revoke_privileges(check_result)
if __name__ == '__main__':
    main()