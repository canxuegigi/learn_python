#!/usr/bin/evn python
#encoding=utf-8
#Author:canxue

int_input = raw_input('输入字符串：')
#数值型字符串
print int_input.isdigit()
#数值和字母
print int_input.isalnum()
#字母
print int_input.isalpha()
#字母全小写
print int_input.islower()
#字母全大写
print int_input.isupper()
print int_input.isspace()
#首字母是否大写,全为字母
print int_input.istitle()

print int_input.center(50,'&')
print int_input.endswith('&')

print '$'.join(('2',))
print '$'.join(['fdsfds','2'])