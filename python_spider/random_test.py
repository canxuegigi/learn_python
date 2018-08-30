#!/usr/bin/evn python
#encoding=utf-8
#Author:canxue


import random

a=['canxue',5,6,'kaka','gigi','gigi','残雪']
s='df4fdsOPsG'
t=('canxue',5,6,'kaka','gigi','gigi','残雪')

#随机生成的一个实数，它在[0,1)范围内
print(random.random())

#左开右闭，若设置了步长，则只能是起始位置，开始的步长n呗，
print(random.randrange(25,29,4))

#左右都闭，整数，必须传两个整数参数，且前一个要小于等于后一个
print(random.randint(21,21))

# Get a random number in the range [a, b) or [a, b] depending on rounding."
print(random.uniform(4,2))

#Choose a random element from a non-empty sequence.,可用于爬虫模拟UA
print(random.choice(a))
print(random.choice(s))
print(random.choice(t))

#from a population sequence or set,选择n个元素
print(random.sample(a,2))
#这种方式很节约空间
print(random.sample(range(100),2))

#将列表的元素顺序打乱(不能是字符串和列表)，返回none，所以不要尝试输出
random.shuffle(a)
print(a)


