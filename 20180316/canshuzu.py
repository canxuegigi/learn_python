#!/usr/bin/evn python
#encoding=utf-8
#Author:canxue

#可以将args/kwargs换成其他名称，但不建议这么干
#将n个位置参数转为元组的方式
def test1(*args):
    print args
#空元组
test1()
test1(1,2,3,4)
test1(*[1,2,3,4])
test1(*(1,2,3,4))

def test2(name,*args):
    print name,args

test2('namme')
test2(1,2,3,4)
test2(*[1,2,3,4])
test2(*(1,2,3,4))

#将n个关键字参数转为字典的方式
def test3(**kwargs):
    print kwargs,kwargs['age']

test3(name='canxue',age=30)
#这样传记得加引号，否则会被当作变量名
test3(**{'name':'canxue','age':30,'sex':"F"})

def test4(name,**kwargs):
    print name,kwargs,kwargs['age']

test4(name='canxue',age=30)
test4('canxue',age=30)
test4(**{'name':'canxue','age':30,'sex':"F"})

def test5(name,*args,**kwargs):
    print name,args,kwargs

test5(name='canxue',age=30)
test5('weizhi','one enough',name='canxue',age=30)
test5('canxue',age=30)
test5(**{'name':'canxue','age':30,'sex':"F"})
