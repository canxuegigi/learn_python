#!/usr/bin/evn python
#encoding=utf-8
#Author:canxue

import time,threading

#wait()是没设置flag就等，而车子在红灯时等，所以红灯时clear()，绿灯时set()
#红灯要等，所以送灯时执行clear()
#黄灯准备，所以送灯时执行clear()
is_green = threading.Event()
is_yellow = threading.Event()

def light():
    count = 0
    while True:
        if count >= 0 and count < 5:
            is_green.clear()
            is_yellow.clear()
            print "\033[41m red light is on...\033[0m"
        elif count >= 5 and count < 7:
            is_yellow.set()
            print "\033[43m yellow light is on...\033[0m"
        elif count >= 7 and count < 17:
            is_green.set()
            is_yellow.clear()
            print "\033[42m green light is on...\033[0m"
        else:
            count = 0

        time.sleep(1)
        count += 1

def car(name):
    while True:
        print is_green.is_set(),is_yellow.is_set()
        if not is_green.is_set() and not is_yellow.is_set():
            print '[%s] sees red light,stop running' %name
            #这里不能加上is_green.wait()，否则黄灯时is_green.wait()卡住，绿灯时is_yellow.wait()卡住，卡住是一直等待，而不是加锁了一直运行
            #is_green.wait()
            is_yellow.wait()
        elif not is_green.is_set() and is_yellow.is_set():
            print '\t [%s] sees yellow light,ready go!!!' %name
            is_green.wait()
        elif is_green.is_set() and not is_yellow.is_set():
            print '\t [%s] sees green light,going running' %name
            time.sleep(1)

red_green = threading.Thread(target=light)
red_green.start()

car_t = threading.Thread(target=car,args=('宝马',))
car_t.start()