#!/usr/bin/env python
# _*_ coding:utf8 _*_
import random
def process(size, total_size):
    percent = size/total_size
    # print(percent)
    percent1 = round(percent*100, 2)
    # print(percent1)
    NUM_OF_STAR = int(percent*100/2)
    # print(NUM)
    print('[%s]%s%%' % ('*'*NUM_OF_STAR, percent1))
process(52674464, 52674464)



