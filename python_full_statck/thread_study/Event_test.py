#!/usr/bin/env python
# _*_ coding:utf8 _*_


import threading
import time
import logging

def worker(event):
    event.wait()
    print('from work')

def write():
    print('form write')

if __name__ == '__main__':
    event = threading.Event()
    t1 = threading.Thread(target=worker, args=(event, ))
    t2 = threading.Thread(target=write)
    t1.start()
    t2.start()
    # t2.join()
    # time.sleep(3)
    event.set()