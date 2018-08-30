#!/usr/bin/evn python
#encoding=utf-8
#Author:canxue

import getpass

try_times=0
log_sucess = 0

while try_times < 3 and log_sucess == 0:
    name_is_locked = 0
    wrong_name = 0
    name=raw_input('your name:')

#判断是否是锁定的用户，返回一个flag,并根据flag循环输入
    f1 = file('lock_info')
    for line in f1.readlines():
        if len(line) > 0:
            if name == line:
                print 'you input name is locked'
                name_is_locked = 1
                break
    f1.close()

    if name_is_locked==1:
        continue

# 判断用户是否存在，返回一个flag,并根据flag循环输入
    f_user_find=file('user_info')
    for line in f_user_find.readlines():
        if name == line.split(' ')[0]:
            break
    else:
        wrong_name = 1

    if wrong_name == 1:
        print 'wrong name'
        continue

# 用户存在且未被锁定，择继续密码的判断，返回一个flag
    while(wrong_name == 0 and name_is_locked == 0 and try_times < 3):
        password = getpass.getpass('your password:')
        f2 = file('user_info')
        for line in f2.readlines():
#            print name == line.split(' ')[0] , password== line.split(' ')[1].strip()
            if name == line.split(' ')[0] and password == line.split(' ')[1].strip():
                print 'welcome %s' %name
                log_sucess = 1
                break
        if log_sucess == 1:
            break

        try_times = try_times +1
#锁定用户
        if try_times == 3:
            f3 = open('lock_info','a')
            print 'lock %s' % name
            f3.write(name+'\n')
            break

