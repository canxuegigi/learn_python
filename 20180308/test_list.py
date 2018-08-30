#!/usr/bin/evn python
#encoding=utf-8
#Author:canxue
"""
list_a = ['a','B','fa','XSA','78','io','02',78]
#这不是浅copy，而是引用
list_b = list_a
print list_a
print list_b
#a=list_a.sort()
#print a
list_a[0] = 'hahah'

print list_a
print list_b


list_a = ['a','B','fa','XSA','78','io','02',78]
list_b = ['aaaaaaaaaaa','bbbbbbbb']
list_c = list_a.extend(list_b)
#print list_c,list_a.extend(list_b)
print list_c,list_a.append(list_b)
print list_a
print list_b



list_a = ['a','B','fa','XSA','78','io','02',78]
list_c = list_a.reverse()
print list_c,list_a.reverse()
print list_a
"""

list_a = ['a','B','fa','XSA','78','io','02',78]
list_c = list_a.sort()
print list_c,list_a.sort()
print list_a