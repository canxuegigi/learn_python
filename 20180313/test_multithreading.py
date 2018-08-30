#!/usr/bin/evn python
#encoding=utf-8
#Author:canxue


import threading,time

def excute_time(name):
    print name," run"
    time.sleep(2)

#单线程方式
start_time = time.time()
excute_time('kaka')
excute_time('canxue')
stop_time = time.time()
print 'total runs time is %s' %(stop_time-start_time)

#多线程方式实例1
t1 = threading.Thread(target=excute_time,args=('kaka',))
t2 = threading.Thread(target=excute_time,args=('canxue',))
start_time = time.time()
t1.start()
t2.start()
stop_time = time.time()
print 'total runs time is %s' %(stop_time-start_time)

#多线程方式实例2
start_time = time.time()
for i in range(50):
    t = threading.Thread(target=excute_time,args=('t-%s' %i,))
    t.start()
    #t.join()加在这里就把程序变为串行了，但我后面还要使用每个t，所以就临时保存啊，这都是线程，所以这里最好使用列表
stop_time = time.time()
#会发现执行的时间很短，也算不是50*2，因为默认主线程启动子线程后就继续执行了，而与子线程就没关系了
print 'total runs time is %s' %(stop_time-start_time)

#多线程方式实例3
thread_list=[]
start_time = time.time()
for i in range(50):
    t = threading.Thread(target=excute_time,args=('t-%s' %i,))
    t.start()
    thread_list.append(t)

print '当前活动的线程：',threading.activeCount()
for t in thread_list:
    t.join()

stop_time = time.time()
print 'total runs time is %s' %(stop_time-start_time)

print '当前活动的线程：', threading.current_thread()
print '当前活动的线程数：',threading.activeCount()










