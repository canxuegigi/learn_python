#!/usr/bin/evn python
#encoding=utf-8
#Author:canxue

"""
理清逻辑，注意时间发生的条件，如下代码队列的大小基本维持在大于等于10且小于等于13左右，因为大于10就会开启狂吃模式
"""

import Queue,time,random,threading

q = Queue.Queue(20)

def producer(name):
    num = 1
    while True:
        if q.qsize() <= 20:
            sleep_time = random.randint(1,3)
            time.sleep(sleep_time)
            q.put('包子%s' %num)
            print '%s 生产了包子%s，现在共 %s 个包子' %(name,num,q.qsize())
            num +=1
        else:
            print '现在共 %s 个包子，不能生产了，仓库没位置了' % (q.qsize())
            time.sleep(5)

def consumer(name):
    #这里不能根据q的空与否，大小为0与否，否则第一次来就退出循环了
    # while not q.empty():
    while True:
        if q.qsize() <= 10:
            c_sleep_time = random.randint(2,5)
            time.sleep(c_sleep_time)
            whice_baozi = q.get()
            print '%s 消费了1个包子，编号为 %s，现在还有 %s 个包子可以吃' %(name,whice_baozi,q.qsize())
        else:
            print '现在共 %s 个包子，快来个人一起吃' % (q.qsize())
            print '开启狂吃模式，狂吃:',q.get()

p = threading.Thread(target=producer,args=('残雪',))
c = threading.Thread(target=consumer,args=('kaka',))

p.start()
c.start()



