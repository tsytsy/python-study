# import bbb
# import 包
# import ccc
# import sys
# print(sys.path)
# # import test1.aaa1
# bbb.func()
# import bbb
# bbb.func()
# bbb.func1()
# from bbb import func as f, func1 as f1
# f()
# f1()
import os, sys
# print(sys.path)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)
print(sys.path)

# from test1 import aaa1, bbb1
# bbb1.func()
# print(bbb1.y)


# 包下的模块导入
'''
包的导入就是在执行__init__.py文件
'''

from test1 import bbb1
# import test1.bbb1

'''
test1下的__init__.py

print('in the test1')
from . import bbb1



# bbb1------>

def func():
    print('from fuc')

y = 1

'''
bbb1.func()

# test1.bbb1.func()
# print(bbb1.y)
from bbb import m
print(m)

