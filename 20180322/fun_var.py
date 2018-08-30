#!/usr/bin/evn python
#encoding=utf-8
#Author:canxue


def bar():
    print 'haha'
print '运行函数:',bar()
print '打印函数内存地址:',bar
a=1
print '变量:',a,id(a)
print '函数:',bar,id(bar),hex(id(bar))

#把标签给一个新变量也可以i的
fun_newname = bar
fun_newname()
