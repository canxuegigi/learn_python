#!/usr/bin/evn python
#encoding=utf-8
#Author:canxue

"""
import threading,time
def excute_time():
    global count
    time.sleep(0.02)
    count += 1
count = 0
for i in range(200):
    t = threading.Thread(target=excute_time)
    t.start()

time.sleep(1)
print 'count:',count
"""




import threading,time
#reentrant lock
user_lock = threading.Lock()

def excute_time():
    user_lock.acquire()
    global count
    time.sleep(0.02)
    count += 1
    user_lock.release()

count = 0

for i in range(200):
    t = threading.Thread(target=excute_time)
    t.start()

#这里值越大，结果越正确，因为sleep的时间越久，线程可能都跑完了
time.sleep(4.5)
print 'count:',count