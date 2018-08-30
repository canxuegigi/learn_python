#!/usr/bin/evn python
#encoding=utf-8
#Author:canxue

#00 04 * * * /usr/bin/python /data/test_ping_zj.py


import commands,datetime,time

"""
#没有自动补0
current_year = datetime.datetime.now().year
current_month = datetime.datetime.now().month
current_day = datetime.datetime.now().day
"""

current_year = datetime.datetime.now().strftime('%Y')
current_month = datetime.datetime.now().strftime('%m')
current_day = datetime.datetime.now().strftime('%d')

#begin_time = datetime.datetime(int(current_year), int(current_month), int(current_day), 3, 58, 0)
#end_time = datetime.datetime(int(current_year), int(current_month), int(current_day),  4, 30, 0)

begin_time = datetime.datetime(int(current_year), int(current_month), int(current_day), 9, 58, 0)
end_time = datetime.datetime(int(current_year), int(current_month), int(current_day), 10, 30, 0)

#不要将open操作放到循环里
#会使用OS的cache，就是写文件操作后，文件里面并没有立即有内容，而是隔一段时间才有，但放循环里就立即有内容，可能是因为每次循环前的open操作会强制刷新cache的内容进文件
f = open('/data/ping_result_'+current_year+current_month+current_day, 'a')
#f = open('ping_result_'+current_year+current_month+current_day, 'a')

while datetime.datetime.now() >= begin_time and datetime.datetime.now() <= end_time:
    excute_time = time.strftime('%Y-%m-%d %X')
    print str(excute_time)
    status, output = commands.getstatusoutput("ping 10.30.21.164 -w 2")
    write_str = str(excute_time) + '\n' + str(status) + '\n' + str(output)+'\n ********************************** \n\n'
    f.write(write_str)
    time.sleep(10)
