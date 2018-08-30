#!/usr/bin/evn python
#encoding=utf-8
#Author:canxue

import MySQLdb

# 创建连接
conn = MySQLdb.connect(host='10.1.4.57', port=3306, user='test_user', passwd='test_user', db='canxue_55',charset='utf8')
# 创建连接的游标
cursor = conn.cursor()  #返回元组，一个记录时就是单个元组，多个记录时就是元组列表

# 执行SQL，并返回收影响行数
effect_row = cursor.execute("select * from test_id_name")

print effect_row

#遍历结果集，均是返回元组；执行一个sql cursor的定位就到了该sql的执行结果;游标一直往前走，执行遍历后位置就会变
print cursor.fetchone()
#默认是1，可在curses.py里配置
print cursor.fetchmany()

set_row = cursor.fetchmany(3)
#cursor.scroll(-4,mode='relative')  # 相对当前位置移动，负数表向前
cursor.scroll(3,mode='absolute') # 相对绝对位置移动，从头开始，此时不能为负
print set_row ,'\n', cursor.fetchmany(3)
print cursor.fetchall()

"""
# 执行SQL，并返回受影响行数
effect_row = cursor.execute("update test_id_name set name = '1.1.1.3' where id = %s", ('11',))

# 多次执行SQL，并返回受影响行数,传入的参数为列表，列表的元素为元组
effect_row = cursor.executemany("insert into test_id_name(id,name)values(%s,%s)", [(12,"1.1.1.11"),(13,"1.1.1.11")])
"""
# 默认开启了事务
conn.commit()
# 关闭游标
cursor.close()
# 关闭连接
conn.close()
