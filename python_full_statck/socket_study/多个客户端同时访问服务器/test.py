#!/usr/bin/env python
# _*_ coding:utf8 _*_

class A:
    x = 1
    y=1000
    def print_x(self):
        print(self.x)
        if hasattr(self,'print_y'):
            func = getattr(self, 'print_y')
            func('666')
            print(func)

    def print_y(self, m):
        print(self.y, m)

class B(A):
    x = 2

b = B()
b.print_x()


import os
os.walk()