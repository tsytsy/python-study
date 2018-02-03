#!/usr/bin/env python
# _*_ coding:utf8 _*_

from multiprocessing import Process
import os
import time

# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))
    print('Parent process %s.' % os.getppid())
    time.sleep(30)

if __name__=='__main__':
    print('main pid is', os.getpid())
    print('Parent process %s.' % os.getppid())

    p = Process(target=run_proc, args=('test',))

    # print('Child process will start.')
    p.start()
    # p.join()
    # print('Child process end.')
    time.sleep(30)



