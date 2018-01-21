import spam
import sys


# money = 1
# def read1():
#     print('=======')
#
#
# read1()



# def g():
#
#     global x
#     print(x)
#
#
# x = 1
# g()

# def fib(n):    # write Fibonacci series up to n
#     a, b = 0, 1
#     while b < n:
#         print(b, end=' ')
#         a, b = b, a+b
#
#
# fib(10)
# L = []
# with open('info.txt', 'r') as f:
#     for i in f:
#         L.append(eval(i))
#
# print(L)

#构造一个信息列表，写入文件中

# name = "'hhh'"
# age = 19
# str1 = '{\'name\': %s,\'age\': %s}' % (name, age)
#
#
# # str1 = '{\'name\':{},\'age\':{}}'
# print(str1)
# with open('info.txt', 'a') as f:
#     f.write(str1+'\n')


#方法2
# L = []
# d = {}
# with open('info1.txt', 'r') as f:
#     for line in f:
#         line = line.strip().split(',')
#         # print(line)
#         d['name'] = line[0]
#         d['age'] = int(line[1])
#         print(d)
#         L.append(d)
# print(L)



L = []
d = {}
with open('info1.txt', 'r') as f:
    # for line in f:
    #     line = line.strip().split(',')
    #     # print(line)
    #     d['name'] = line[0]
    #     d['age'] = int(line[1])
    #     print(d)
    #     L.append(d)


    lines = [line.split(',') for line in f]
    res = [{'name': line[0], 'age': line[1]} for line in lines]
print(res)


d = {'name': 'tsy', 'age': 18}

L = d.values()
for i in L:
    print(i)