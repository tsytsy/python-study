#!/usr/bin/env python
# _*_ coding:utf8 _*_

# import queue
# # q = queue.Queue(3)
# q = queue.LifoQueue(3)
# q.put(1111)
# q.put('123')
# q.put('ads')
# # q.put('lyt', False)
#
# print(q.get())
# print(q.get())
# print(q.qsize())
# print(q.get())
# print(q.get(timeout=1))


import time, random
import queue, threading

q = queue.Queue()

def Producer(name):
  count = 0
  while count < 10:
    print("making........")
    # time.sleep(random.randrange(3))
    time.sleep(2)
    q.put(count)

    print('Producer %s has produced %s baozi..' % (name, count))
    count += 1
    #q.task_done()
    #q.join()
    print("ok......")

def Consumer(name):
  count = 0
  while count < 10:
    # time.sleep(random.randrange(4))
    time.sleep(1)
    if not q.empty():
        data = q.get()
        #q.task_done()
        #q.join()
        print(data)
        print('\033[32;1mConsumer %s has eat %s baozi...\033[0m' %(name, data))
    else:
        print("-----no baozi anymore----")
    count += 1


p1 = threading.Thread(target=Producer, args=('A',))
c1 = threading.Thread(target=Consumer, args=('B',))
# c2 = threading.Thread(target=Consumer, args=('C',))
# c3 = threading.Thread(target=Consumer, args=('D',))
p1.start()
c1.start()
# c2.start()
# c3.start()