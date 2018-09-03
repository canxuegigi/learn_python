#!/usr/bin/evn python
#encoding=utf-8
#Author:canxue

"""
先认真分析需求，画出流程图
处理过程中使用正确的数据类型和操作方式
始终注意输入与输出

学会分析，举一反三

"""

stat_dict = {}
row_num = 0
black_chart = ['，','\n','。','“','”','：','…']

"""
UnicodeDecodeError: 'gbk' codec can't decode byte 0x80 in position 4: illegal multibyte sequence
windows上默认使用gbk编码打开文件，而文件以前是utf-8的编码，所以报错，两种方式
修改文件的编码
指定打开文件的编码：fr = open('文件名','r',encoding='utf-8'
"""
fr = open('调教初唐.txt','r')
for line in fr:
    line.strip()
    for i in line:
        if i not in black_chart:
            if i in stat_dict:
                stat_dict[i] = stat_dict[i] + 1
            else:
                stat_dict[i] = 1
        else:
            continue
    row_num = row_num + 1
fr.close()

print('总共遍历 %s 行'%row_num)

#字典是无序的
#stat_dict.items() 转为迭代器
result_dict = sorted(stat_dict.items(),key = lambda item:item[1],reverse=True)

for i in result_dict:
    print(i)


