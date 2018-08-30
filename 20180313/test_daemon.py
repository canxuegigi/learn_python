#!/usr/bin/evn python
#encoding=utf-8
#Author:canxue

import threading,time

def excute_time(name):
    print name," run"
    time.sleep(5)

thread_list=[]
start_time = time.time()
for i in range(50):
    t = threading.Thread(target=excute_time,args=('t-%s' %i,))
    #t.setDaemon(True)
    t.start()
    thread_list.append(t)
stop_time = time.time()
print 'total runs time is %s' %(stop_time-start_time)

print '当前活动的线程：', threading.current_thread()
print '当前活动的线程数：',threading.activeCount()
