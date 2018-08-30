#!/usr/bin/evn python
#encoding=utf-8
#Author:canxue

import  time

def timmer(func):
    def warpper(*args,**kwargs):
        start_time = time.time()
        func()
        stop_time = time.time()
        print 'function runs time is %s' %(stop_time-start_time)
    return  warpper

@timmer
def sleep_fun():
    time.sleep(3)
    print 'fun runs end'

sleep_fun()

add_num=lambda x:x+3
print add_num(2)






