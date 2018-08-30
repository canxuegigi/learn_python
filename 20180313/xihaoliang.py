#!/usr/bin/evn python
#encoding=utf-8
#Author:canxue

import threading, time,random

def run(n):
    semaphore.acquire()
    sleep_time = random.randint(1,10)
    print("run the thread: %s" % n, 'sleep_time:', sleep_time)
    time.sleep(sleep_time)
    semaphore.release()

if __name__ == '__main__':
    # 最多允许5个线程同时运行
    semaphore = threading.BoundedSemaphore(5)
    for i in range(20):
        t = threading.Thread(target=run, args=(i,))
        t.start()
        #t.join()

while threading.active_count() != 1:
    pass  # print threading.active_count()
else:
    print('----all threads done---')
