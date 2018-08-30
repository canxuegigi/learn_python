#!/usr/bin/evn python
#encoding=utf-8
#Author:canxue

import pandas as pd

all_data = pd.read_csv('E:\\test_canxue.csv',header=None)
all_data2 = pd.read_csv('E:\\test_canxue.csv',names=['create_time','update_time'])

#默认不含表头,即默认是将第一行作为表头，不作为数据，而操作都是针对数据的
#一下结果根据header=None的设置与否，会有差别
print len(all_data),type(all_data)
#print all_data.head(),all_data.tail()
#若没有设置header=None，则第一行作为表头，则all_data.head(1)返回第二行数据(即认为真正数据从第二行开始)
#若设置header=None，则第一行作为数据开始的地方，则all_data.head(1)返回第二行数据
print all_data2







