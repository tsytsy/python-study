# with open('saralies.txt', 'r', encoding='utf8') as f:
#     res = [line.split() for line in f]
#     saralies = [{'name': i[0], 'sex': i[1], 'age': int(i[2]), 'salary': int(i[3])} for i in res]
#
# # print(saralies)
# # print(max(saralies, key=lambda x: x['salary']))
# # print(min(saralies, key=lambda x: x['age']))
#
# f = map(lambda x: x['name'].title(), saralies)
# print(list(f))
# # def upperFirst(x):
# #     x['name'] = x['name'].title()
# #     return x
#
# f = filter(lambda x: x['name'][0] != 'a', saralies)
# print(list(f))
#
# # f = map(lambda x: x['name'], saralies)
# # print(list(f))

# l =[1, 2, [3, [4, 5, 6, [7, 8, [9, 10, [11, 12, 13, [14, 15]]]]]]]
#
# def search(l):
#     for item in l:
#         if type(item) is list:
#             search(item)
#         else:
#             print(item)
#
# search(l)
# def isnumber(aString):
#     try:
#         float(aString)
#         return True
#     except:
#         return False
#
# def a():
#
#     while True:
#         overdraft = input('>>输入用户的透支额，退出请按q:')
#         if overdraft == 'q':
#             return
#         elif not isnumber(overdraft):
#             print('not a number')
#             continue
#         break
#     print(overdraft)
#
#
# flag = True
# while flag:
#     a = input('>>')
#     if a not in ['1','2']:
#         continue
#     flag = False
# else:
#     print('***************')
#
# print(a)

#
# for i in range(1,10,2):
#     print(i)

# def next(a, b=1, c=2, d=3, *args, **kwargs):
#     print(a)
#     print(b)
#     print(c)
#     print(d)
#     print(args)
#     print(kwargs)
#
#
# next(1,c=2,d=4,x=3)
import sys
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ' a test module '
#
# __author__ = 'Michael Liao'
#
# import sys
#
#
# def test():
#     '''
#     test a moudle
#     :return: None
#     '''
#     args = sys.argv
#     print(args)
#     for i in args:
#         print(i)
#     if len(args)==1:
#         print('Hello, world!')
#     elif len(args)==2:
#         print('Hello, %s!' % args[1])
#     else:
#         print('Too many arguments!')
#
#
# print(test.__doc__)
# test()
# print(sys.path)
# print(test.__name__)

# def sayhi():
#     print('Hi,this is a moudle')
#
#
# version = '0.1'


with open('saralies.txt', 'r') as f:
    # for line in f:
    print(f)
    # for line in f.readlines():
    f.seek(0, 0)
    print(f.readlines())