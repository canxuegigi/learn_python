#!/usr/bin/evn python
#encoding=utf-8
#Author:canxue

import time
"""第一版"""
print '第一版'
def test1():
    print 'in the test1'
    time.sleep(2)
test1()

"""第二版加上时间功能"""
print '第二版'
def test1():
    print 'in the test1'
    time.sleep(2)

def timmer(func_name):
    start_time = time.time()
    func_name()
    stop_time = time.time()
    print 'test1 run time:',stop_time - start_time
#这改变了调用方式
timmer(test1)

"""第三版加上时间功能，因为第二版改变了调用方式，这需要返回函数的内存才可以"""
print '第三版'
def test1():
    print 'in the test1'
    time.sleep(2)

def timmer(func_name):
    def zhuangshi():
        start_time = time.time()
        func_name()
        stop_time = time.time()
        print 'test1 run time:',stop_time - start_time
    return zhuangshi

test1 = timmer(test1)
test1()

"""第四版，第三版中实现了装饰器的效果，但若test1函数有参数，则就会报错，而且被装饰的函数的传入参数千差万别，所以参数组有用了"""

print '第四版'
def test1(name):
    print name,' in the test1'
    time.sleep(2)

def test2(name,age):
    print name,' in the test2'
    time.sleep(2)

def timmer(func_name):
    def zhuangshi(*args,**kwargs):
        start_time = time.time()
        func_name(*args,**kwargs)
        stop_time = time.time()
        print func_name,'run time:',stop_time - start_time
    return zhuangshi

test1 = timmer(test1)
test1('kaka')

test2 = timmer(test2)
test2('gigi','40')

