#!/usr/bin/evn python
#encoding=utf-8
#Author:canxue

import time

def fun_test1():
    """注释"""
    return 'first',2,('fds',),{'name':'canxue'}

def fun_test2():
    """注释"""
    return fun_test1

def fun_test3():
    """注释"""
    return fun_test1()

print fun_test1()
print fun_test2()
print fun_test3()




def my_fun(name,age=28,address='sichuan'):
  print 'name is ',name,'age is ',age,'adress is ',address

my_fun('canxue')
my_fun('canxue',address='suining')
my_fun(age=58,name='kaka')
my_fun('gigi',name='dicky')	#报错，既然要覆写就别给值了，注意顺序
my_fun(name='dicky','gigi')	#报错，既然要覆写就别给值了，注意顺序