#!/usr/bin/evn python
#encoding=utf-8
#Author:canxue

import time

#列表生成式
a = [i*2 for i in xrange(10)]

def add_two(var_num):
    var_num = var_num + 2
    return var_num
b = [add_two(i) for i in xrange(10)]

print a
print b

g = (i*2 for i in xrange(10))
print type(g)



def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print b
        a, b = b, a + b
        n = n + 1
    return 'done'
fib(10)

start_time = time.time()
a=[i for i in range(100000000)]
stop_time = time.time()
print 'list:',stop_time - start_time

start_time = time.time()
g=(i for i in range(100000000))
stop_time = time.time()
print 'g:',stop_time - start_time