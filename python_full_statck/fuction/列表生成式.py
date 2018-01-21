'''
列表生成式式生成列表的一种简易形式，类似于变量的声明
'''

# #生成一个平方数的列表
#
# L = []
# for i in range(1, 11):
#     L.append(i*i)
# print(L)
#
# '''
# 生成式表达
# '''
# L = [i*i for i in range(1, 11)]
# print(L)

'''
列表生成式生成的是一个列表，但是列表中数据会一次性读取，数据太多会造成电脑卡顿
将列表变成生成器表达式，每次只生成一个数据，需要的时候再根据区生成器表达式中取
'''
# L = (i*i for i in range(1, 11))
# print(L)
# for i in L:
#     print(i)
# L1 = []
# L = [1, 2, 3, 4]
# s = 'hello'
# for i in L:
#     if i > 2:
#         for j in s:
#             print((i, j))
#             L1.append((i, j))

# print(L1)

# L1 = [(i, j) for i in L if i > 2 for j in s]
# print(L1)

'''
怎么去掉文件中的空格和换行符，
'''
# L = []
# with open('cache.txt') as f:
#     for line in f:
#         # print(line)
#         line = line.strip()
#         L.append(line)
# print(L)

'''
用生成式来实现
apple 10 3
tesla 1000000 1
mac 3000 2
lenovo 30000 3
chicken 10 3
'''
# with open('cache.txt') as f:
#     L = (line.strip() for line in f)
# for line in L:
#     print(line)

with open('data') as f:
    res = (line.strip().split() for line in f)
    dic_g = ({'name': i[0], 'price': i[1], 'count': i[2]} for i in res)
    # for i in dic_g:
    #     print(i)

for i in dic_g:
    print(i)  