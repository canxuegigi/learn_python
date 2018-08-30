#!/usr/bin/evn python
#encoding=utf-8
#Author:canxue


import  re
"""
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

mo = phoneNumRegex.match('415-555-424')


print(mo.groups())
print(mo.group(2))
print(mo.group(1))
"""
""""""
s1 = r'ab*'
s2 = r'ab*?'

re_o1 = re.compile(s1)
re_o2 = re.compile(s2)

m1 = re_o1.match('2abbbbbbbbb')
m2 = re_o2.match('abbbbbbbbb')

print(m1)
print(m2.group())



"""
中文 [u4e00-u9fa5]


s = r'[\u4e00-\u9fa5]+'
re_o = re.compile(s)
m = re_o.match(u'你好，我的adfds世界，哈哈！',3,20)
print(m)
"""

