#!/usr/bin/env python
# _*_ coding:utf8 _*_

import threading
import time
metux1 = threading.RLock()
# metux2 = threading.Lock()


class MyThread(threading.Thread):
    def __init__(self):
        super(MyThread, self).__init__()

    def run(self):
        self.func1()
        self.func2()

    def func1(self):
        metux1.acquire()
        # time.sleep(2)
        print('I am in lock 2')
        metux1.acquire()
        print('I am in metux 1')
        metux1.release()
        metux1.release()

    def func2(self):
        metux1.acquire()
        # time.sleep(3)
        print('I am in lock 1')
        metux1.acquire()
        print('I am in metux 2')
        metux1.release()
        metux1.release()

if __name__ == '__main__':
    for i in range(10):
        t = MyThread()
        t.start()