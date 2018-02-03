#!/usr/bin/env python
# _*_ coding:utf8 _*_

'''
1.协程不需要多线程，自己控制在哪里切换
2 yield可以保存状态，不需要锁来保存状态
3. yield不能够进行IO操作

'''


def consumer():
    r = 'ok'
    while True:
        x = yield r
        r = x


def product(c):
    next(c)
    for i in range(6):
        # print(a)
        b = c.send(i)
        print(b)

if __name__ == '__main__':
    c = consumer()
    product(c)