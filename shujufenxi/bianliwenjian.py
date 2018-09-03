#!/usr/bin/evn python
#encoding=utf-8
#Author:canxue

f = open('调教初唐.txt','r')
row_num = 1
for i in f.readline():
    if row_num < 150:
        print('row_num:',row_num,i)
        row_num = row_num + 1


f = open('调教初唐.txt','r')
row_num = 1
while True:
    line = f.readline()
    if line:
        print('row:',row_num,line)
        row_num = row_num + 1
    else:
        break

f = open('调教初唐.txt','r')
row_num = 1
for i in f.readlines():
    if row_num < 150:
        print('row_num:',row_num,i)
        row_num = row_num + 1

f = open('调教初唐.txt','r')
row_num = 1
for i in f:
    if row_num < 150:
        print('row_num:',row_num,i)
        row_num = row_num + 1