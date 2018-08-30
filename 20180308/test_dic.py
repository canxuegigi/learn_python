#!/usr/bin/evn python
#encoding=utf-8
#Author:canxue

stu={'zhengjing':30,'kaka':40,'dicky':50}

print stu
print stu.items()

#stu.popitem()

print stu.setdefault('kaka','25')
print stu.update()

print stu
print 'zhengjing1' in stu
print  stu.has_key('zhengjing')

for i in stu:
    print i




