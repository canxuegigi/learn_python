#!/usr/bin/evn python
#encoding=utf-8
#Author:canxue


def bar():
    print 'in the bar'
    #这里相当于局部变量，所以外层调用不了
    def boo():
        print 'int the boo'

    #boo()

bar()
#boo()