'''
要求:
从文件中取出每一条记录放入列表中,
列表的每个元素都是{'name':'egon','sex':'male','age':18,'salary':3000}的形式

2 根据1得到的列表,取出薪资最高的人的信息
3 根据1得到的列表,取出最年轻的人的信息
4 根据1得到的列表,将每个人的信息中的名字映射成首字母大写的形式
5 根据1得到的列表,过滤掉名字以a开头的人的信息
6 使用递归打印斐波那契数列(前两个数的和得到第三个数，如：0 1 1 2 3 4 7...)

7 一个嵌套很多层的列表，如l=［1,2,[3,[4,5,6,[7,8,[9,10,[11,12,13,[14,15]]]]]]］，用递归取出所有的值

'''
# L = []
# d={}
# with open('saralies.txt', 'r', encoding='utf8') as f:
#     for line in f:
#         line = line.split()
#         d['name'] = line[0]
#         d['sex'] = line[1]
#         d['age'] = line[2]
#         d['salary'] = line[3]
#         L.append(d)
#
# print(L)
#列表生成式

# # L = [x*x for x in range(10)]
#
# with open('saralies.txt', 'r', encoding='utf8') as f:
#     res = [line.split() for line in f]
#     saralies = [{'name': i[0], 'sex': i[1], 'age': int(i[2]), 'salary': int(i[3])} for i in res]
#
# print(saralies)
# print(max(saralies, key=lambda x: x['salary']))
# print(min(saralies, key=lambda x: x['age']))
#
# # f = map(lambda x: x['name'].title(), saralies)
# def upperFirst(x):
#     x['name'] = x['name'].title()
#     return x
# f = map(upperFirst, saralies)
# print(list(f))
#
# f = filter(lambda x: x['name'][0] != 'a', saralies) m
# print(list(f))

def fab(n):
    # print('===>')
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fab(n-1)+fab(n-2)
# print(fab(5))

for i in range(1, 10):
    print(fab(i), end=' ')


# l = [1, 2, [3, [4, 5, 6, [7, 8, [9, 10, [11, 12, 13, [14, 15]]]]]]]
#
# def search(l):
#     for item in l:
#         if type(item) is list:
#             search(item)
#         else:
#             print(item)
#
# search(l)