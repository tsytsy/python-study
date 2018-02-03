#!/usr/bin/env python
# _*_ coding:utf8 _*_

import time
import threading

def subnum():
    global num #在每个线程中都获取这个全局变量
    # num-=1
    print('OK')
    lock.acquire()
    temp = num
    time.sleep(0.001)
    num = temp-1  # 对此公共变量进行-1操作
    lock.release()

lock = threading.Lock()
num = 100  # 设定一个共享变量
if __name__ == '__main__':
    thread_list = []

    for i in range(100):
        t = threading.Thread(target=subnum)
        t.start()
        thread_list.append(t)

    for t in thread_list: #等待所有线程执行完毕
        t.join()

    print(len(thread_list))
    print('Result: ', num)
