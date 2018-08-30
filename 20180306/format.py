#!/usr/bin/evn python
#encoding=utf-8
#Author:canxue

import getpass

"""
a=range(10)
for i in a:
    print i
    print '----------'
"""
name=raw_input('your name:')
age=int(raw_input('your age:'))
passworld=getpass.getpass('your pass:')

info1="""
    name=%s
    age=%d
"""
print info1 %(name,age)

info2="""
    name={new_name}
    age={new_age}
""".format(new_name=name,new_age=age)
print info2

info3="""
    name={0}
    age={1}
    password={2}
""".format(name,age,passworld)
print info3
