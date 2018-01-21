#_*_ coding:utf-8 _*_
#如何便利一个序列
#序列有以下几种，字符串、列表、元组、字典、集合，前面三种是有序的序列，后面两种是无效的序列
#对于有序的序列，可以采用索引（下标）的方式来遍历所有的元素
# L = [1, 45, 36, 42]
# for i in range(len(L)):
#     print(L[i])
#
# count = 0
# while count < len(L):
#     print(L[count])
#     count += 1

#那么对于一个无序的序列应该怎么才能遍历所有的元素
d = {'a': 1, '2': 22, 'key': 'value'}

'检测一个对象是否可迭代方法__iter__,返回值是迭代器'
# i = d.__iter__() #i 是一个迭代器
'使用next函数取得迭代器的下一个key值'

# print('>>>>>>', len(d))
# while True:
#     try:
#         print(next(i))
#     except StopIteration:
#         break
# for i in d:
#     print(i, d[i])
#
# '一个列表也是一个迭代器'

# L = [1, 45, 36, 42]
# i = L.__iter__()
# while True:
#     try:
#         print(next(i))
#     except StopIteration:
#         break
i = d.__iter__()
for e in i:  #L.__iter__() for 也是根据next取迭代器中的下一个值的
    try:
        print(e)
    except StopIteration:
        print('666')


# i = d.__iter__()
# i.__next__
# next(i)

'''
迭代，是可以进行重复取值的，也就数有多个值，在python中，整形、浮点型、布尔型都只能存取一个数
而字符串、列表、元组、字典、集合是由多个元素组成，那么理论上就可以认为具备迭代的潜力，那么真正判断一个
对象是否可迭代的是这个对象是否存在__iter__函数，此函数是一个内置函数，会生成一个迭代器iterator，真正进行
迭代的是迭代器，迭代器内置了一个__next__函数，也可以使用内置函数next来操作迭代器，使用for,sum等函数实际上
就是对操作器进行了next操作。
'''
