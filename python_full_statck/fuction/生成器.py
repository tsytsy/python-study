#_*_ coding:utf-8 _*_
'''
生成器：
函数生成器：生成的是一个迭代器，说明有多个值
yield有两个作用：1、说明该函数是一个生成器函数；2. 在yield的处就会返回一个迭代器元素
前面讲的可迭代对象基本上都是固定了长度，但是生成器开始的时候是没有长度的，你需要多少次迭代运行多少次next()就好了
因为函数每一次都会返回一个
函数的执行时由next(g)来触发的
最难理解的就是generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
这是因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误。
可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，
只有在需要返回下一个数据时它才会计算。

Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。
'''
from collections import Iterator
def count():
    N = 0
    while True:
        # print('*****')
        yield N
        N += 1



g = count()

# 'g是一个迭代器'
print(isinstance(g, Iterator))
# # for i in g:
# #     print(i)
print(next(g))
print(next(g))
print(next(g))
#
# c1 = 5
# while c1 > 0:
#     print(c1)
#     c1 -= 1
#     if c1 < 3:
#         print(next(g))


# def foo():
#     print('one')
#     yield 1
#     print('two')
#     yield 2
#     print('3')
#     yield 3
#
#
# g = foo()
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))



#利用生成器实现tail功能
# def tail(path):
#     with open(path, 'r', encoding='utf8') as f:
#         f.seek(0, 2)
#         while True:
#             line = f.readline()
#             if not line:
#                 continue
#             else:
#                 yield line
#                 print('again')
#
#
# g = tail('cache.txt')
# print(next(g))
# print(next(g))
