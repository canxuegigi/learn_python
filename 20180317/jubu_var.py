#!/usr/bin/evn python
#encoding=utf-8
#Author:canxue

#实参传到函数后，函数里的name就是局部变量，而不是函数外层的name，即函数就是函数里的变量的作用域
def change_name(name):
    print 'before change:',name
    name = 'HAHA'
    print 'after name:',name

name = 'haha'
change_name(name)
print name

#函数里可以访问全局变量，但默认不能修改，若要修改则需要在函数里声明 global var_name
country = 'china'
def access_global_var():
    #当局部变量和全局变量同名的时候，局部变量会覆盖全局变量
    #global country
    print 'country var:',country
    #默认情况下，函数里修改全局变量会报错，UnboundLocalError: local variable 'country' referenced before assignment
    country = 'CHINA'

access_global_var()
print country


#函数里可以访问全局变量，但默认不能修改，若要修改则需要在函数里声明 global var_name
country = 'china wai'
def fun_in_out():
    country = 'china li'
    print 'fun in:',country

fun_in_out()
print 'fun out:', country