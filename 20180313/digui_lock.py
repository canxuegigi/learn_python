#!/usr/bin/evn python
#encoding=utf-8
#Author:canxue

"""
说白了就是在一个大锁中还要再包含子锁
"""
import threading, time

def run1():
    print("grab the first part data")
    lock.acquire()
    global num
    num += 1
    lock.release()
    return num

def run2():
    print("grab the second part data")
    lock.acquire()
    global num2
    num2 += 1
    lock.release()
    return num2

def run3():
    lock.acquire()
    res = run1()
    print('--------between run1 and run2-----')
    res2 = run2()
    lock.release()
    print(res, res2)

if __name__ == '__main__':
    num, num2 = 0, 0
    lock = threading.Lock()
    #lock = threading.RLock()
    for i in range(100):
        t = threading.Thread(target=run3)
        t.start()

while threading.active_count() != 1:
    print(threading.active_count())
else:
    print('----all threads done---')
    print(num, num2)