#_*_ceding:utf-8 _*_
'''
生成器是一个迭代器，但是不需要事先准备好一个迭代的长度，生成会根据需要自己生成一个序列的长度
这样生成器(迭代器)就会节省内存
使用迭代器需要用到next(iterabor),这个操作会去再次的运行函数
'''


# def range1(start, stop, step=1):
#     if start > stop:
#         return 'error, stop should be bigger than start'
#     n = start
#     while n < stop:
#         yield n
#         n += step
#
#
# for i in range1(1, 7, 2):
#     print(i)
#     # if i == 3:
#     #     break

#模拟管道，实现功能:tail -f access.log | grep '404'  数据流形式，车间流模式
# def my_tail(path):
#     with open(path, 'r', encoding='utf8') as f:
#         f.seek(0, 2)
#         while True:
#             line = f.readline()
#             if not line:
#                 continue
#             yield line
#
#
# def my_grep(pattern, target):
#      for line in target:
#         if pattern in line:
#             yield line
#
#
# for line in my_grep('asd', my_tail('cache.txt')):
#     print(line)

#协程函数：在函数中yield用在表达式中的称为协程函数
'''
send 和next的异同
1. 都可以从yield处开始进行下一次数据获取
2. send可以给yield的变量赋值，然后继续执行程序，等到下一次yield
'''


def init(func):
    def wrapper(*args, **kwargs):
        g = func(*args, **kwargs)
        next(g)
        return g
    return wrapper


@init   #eater = init(eater)
def eater():
    food_list = []
    while True:
        food = yield food_list
        food_list.append(food)


o = eater()
print(o.send('egg'))
print(o.send('meat'))

#实现功能：grep  -rl  'python'  /etc
'''
查找一个文件中所有文件中存在'python'的语句
'''
# import os

# def init(func):
#     def wrapper(*args, **kwargs):
#         g = func(*args, **kwargs)
#         next(g)
#         return g
#
# @init


import os
import time
# def search(file_path):
#     '''
#     :param path:需要查找的文件的路径
#     :return:
#     '''
#     path = ''
#     g = os.walk('D:\\a')
#
#     for i in g:
#         path_list = []
#         # print(i)
#         # print(i[2])
#         for j in range(len(i[2])):
#             # print(j)
#             path_list.append(i[0] + '\\' + i[2][j])
#         yield path_list
#
#
# def find(pattern, path_list):
#     path_list2 = []
#     for path in path_list:
#         with open(path, 'r') as f:
#             for line in f.readlines():
#                 if pattern in line:
#                     path_list2.append(path)
#                     break
#     yield path_list2
#
#
# def printer(path_list):
#     yield path_list
#
#
# for i in search('D:\\a'):
#     for j in find('python', i):
#         for k in printer(j):
#             print(k)

import os
# import time
# def search(file_path):
#     '''
#     :param path:需要查找的文件的路径
#     :return:
#     '''
#     g = os.walk('D:\a')
#     path_list = []
#     for i in g:
#         for j in range(len(i[2])):
#             path_list.append(i[0] + "'\'" + i[2][j])
#
#
# def find(pattern, path_list):
#     path_list2 = []
#     for path in path_list:
#         with open(path, 'r') as f:
#             for line in f.readlines():
#                 if pattern in line:
#                     path_list2.append(path)
#                     break
#     yield path_list2
#
#
# def printer(path_list):
#     yield path_list
#
#
# for i in search('D:\\a'):
#     for j in find('python', i):
#         for k in printer(j):
#             print(k)

#模拟数据流传输的概念，
# def my_tail(file_path):
#     '''
#     源源不断的取最后一行数据,生成器用来生成数据的，那么怎么样可以不断的生成数据呢？使用next(g)不断的取调用函数
#     函数不断的返回值，就可以不停的进行调用
#     :param file_path:
#     :return:
#     '''
#     with open(file_path, 'r', encoding='utf8') as f:
#         f.seek(0, 2)
#         while True:
#             line = f.readline()
#             if not line:
#                 continue
#             yield line
#
#
# def my_grep(pattern, line):
#     for lines in line:
#         if pattern in lines:    #next(g)
#             print(lines)
#
# g = my_tail('cache.txt')
# my_grep('hello', g)

