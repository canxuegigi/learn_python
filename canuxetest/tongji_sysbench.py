#!/usr/bin/evn python
#encoding=utf-8
#Author:canxue

import os

#定义计数tps和tps的记录
t_one,t_two,t_three,t_four,t_five,t_six,t_seven,t_eight,t_nine,t_ten,t_gt_ten=0,0,0,0,0,0,0,0,0,0,0
q_one,q_two,q_three,q_four,q_five,q_six,q_seven,q_eight,q_nine,q_ten,q_gt_ten=0,0,0,0,0,0,0,0,0,0,0


os.system("more sysbench.log | grep tps | awk '{print $7,$9}' > sysbench_result")

file_line = 0

f = file('sysbench_result','r')
for i in f.readlines():
    file_line = file_line + 1
    i = i.strip().split(' ')

    """统计tps"""
    tps = float(i[0])
    if tps < 1000:
        t_one = t_one + 1
    if tps >= 1000 and tps < 2000:
        t_two = t_two + 1
    if tps >= 2000 and tps < 3000:
        t_three = t_three + 1
    if tps >= 3000 and tps < 4000:
        t_four = t_four + 1
    if tps >= 4000 and tps < 5000:
        t_five = t_five + 1
    if tps >= 5000 and tps < 6000:
        t_six = t_six + 1
    if tps >= 6000 and tps < 7000:
        t_seven = t_seven + 1
    if tps >= 7000 and tps < 8000:
        t_eight = t_eight + 1
    if tps >= 8000 and tps < 9000:
        t_nine = t_nine + 1
    if tps >= 9000 and tps < 10000:
        t_ten = t_ten + 1
    if tps >= 10000 :
        t_gt_ten = t_gt_ten + 1


    """统计qps"""
    qps = float(i[1])
    if qps < 10000:
        q_one = q_one + 1
    if qps >= 10000 and qps < 20000:
        q_two = q_two + 1
    if qps >= 20000 and qps < 30000:
        q_three = q_three + 1
    if qps >= 30000 and qps < 40000:
        q_four = q_four + 1
    if qps >= 40000 and qps < 50000:
        q_five = q_five + 1
    if qps >= 50000 and qps < 60000:
        q_six = q_six + 1
    if qps >= 60000 and qps < 70000:
        q_seven = q_seven + 1
    if qps >= 70000 and qps < 80000:
        q_eight = q_eight + 1
    if qps >= 80000 and qps < 90000:
        q_nine = q_nine + 1
    if qps >= 90000 and qps < 100000:
        q_ten = q_ten + 1
    if qps >= 100000 :
        q_gt_ten = q_gt_ten + 1

print '文件共%s行' %file_line

print '********tps result:********'
print '<1k:',t_one
print '1k-2k:',t_two
print '2k-3k:',t_three
print '3k-4k:',t_four
print '4k-5k:',t_five
print '5k-6k:',t_six
print '6k-7k:',t_seven
print '7k-8k:',t_eight
print '8k-9k:',t_nine
print '9k-10k:',t_ten
print '>10k:',t_gt_ten

print '********qps result:********'
print '<1w:',q_one
print '1w-2w:',q_two
print '2w-3w:',q_three
print '3w-4w:',q_four
print '4w-5w:',q_five
print '5w-6w:',q_six
print '6w-7w:',q_seven
print '7w-8w:',q_eight
print '8w-9w:',q_nine
print '9w-10w:',q_ten
print '>10w:',q_gt_ten
