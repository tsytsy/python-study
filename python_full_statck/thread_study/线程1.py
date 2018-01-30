#!/usr/bin/env python
# _*_ coding:utf8 _*_

import threading
import time

# def tingge():
#     print('听歌')
#     time.sleep(3)
#     print('听歌结束')
#
#
def xieboke():
    print('写博客')
    time.sleep(5)
    print('写博客结束')
#
# # 创建线程方法一: 调用thread.Threading类
# t1 = threading.Thread(target=tingge)
# t2 = threading.Thread(target=xieboke)
# s = time.time()
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(time.time() - s)
# print('ending')

# 创建线程方法二:继承thread.Threading类

class MyThread(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, *, daemon=None, num):
        super(MyThread, self).__init__(group, target, name,
#                  args, kwargs)
#         self.num = num
#
#     # def run(self):
#     #     print('num is:', self.num)
#     #     time.sleep(3)
#
#     def run(self):
#         try:
#             print(self.num)
#             if self._target:
#                 self._target(*self._args, **self._kwargs)
#         finally:
#
#             # Avoid a refcycle if the thread is running a function with
#             # an argument that has a member that points to the thread.
#             del self._target, self._args, self._kwargs
# if __name__ == '__main__':
#
#     mythead = MyThread(target=xieboke ,num=32)
#     mythead.start()
#     print('ending')


# JOIN && SETDEAMON

'''
将线程声明为守护线程，必须在start() 方法调用之前设置，如果不设置为守护线程程序会被无限挂起。
当我们在程序运行中，执行一个主线程，如果主线程又创建一个子线程，主线程和子线程 就分兵两路，分别运行，那么当主线程完成
想退出时，会检验子线程是否完成。如果子线程未完成，则主线程会等待子线程完成后再退出。但是有时候我们需要的是只要主线程
完成了，不管子线程是否完成，都要和主线程一起退出，这时就可以 用setDaemon方法啦
守护线程有可能在主线程完成之前就执行完程序了，
'''
import threading
from time import ctime, sleep
import time

def Music(name):

        print("Begin listening to {name}. {time}".format(name=name,time=ctime()))
        sleep(3)
        print("end listening {time}".format(time=ctime()))

def Blog(title):

        print("Begin recording the {title}. {time}".format(title=title,time=ctime()))
        sleep(5)
        print('end recording {time}'.format(time=ctime()))


threads = []


t1 = threading.Thread(target=Music, args=('FILL ME',))
t2 = threading.Thread(target=Blog, args=('PYTHON',))

threads.append(t1)
threads.append(t2)

if __name__ == '__main__':

    # t1.setDaemon(True)
    t2.setDaemon(True)
    for t in threads:

        #t.setDaemon(True) #注意:一定在start之前设置
        t.start()

        # t.join()

    # t1.join()
    # t2.join()    #  考虑这三种join位置下的结果？
    print(t1.is_alive())
    t1.setName('lyt')
    print(t1.getName())
    print("all over %s" %ctime())
    print(threading.current_thread())
    print(threading.active_count())
    print(threading.enumerate())

