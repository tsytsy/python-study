# 定义一个整形列表类型
# from collections import Iterable
#
#
from collections import Iterable


class List(list):
    def __init__(self, L):
        if not isinstance(L, Iterable):
            raise ValueError('argument must be a iterable')
        for i in L:
            if not isinstance(i, int):
                raise ValueError('element must be int')
            self.append(i)

    def append(self, value):
        if not isinstance(value, int):
            raise ValueError('value must be int')
        super(List, self).append(value)

    def insert(self, index, value):
        if not isinstance(index, int):
            raise TypeError('must be int')
        if not isinstance(value, int):
            raise TypeError('must be int')
        super().insert(index, value)

    @property
    def mid(self):
        return self.index(len(self)//2)


# l = List((1, 1))
# l.append(1)
# l.insert(-1, 2)
# print(l)
# print(l.mid)

# l = List([1, 2, 3])
# print(l.__dict__)

# f = open('info.txt', 'a')
# print(f)
# f.write('aaaa')




# import time
# class Open:
#     def __init__(self, filepath, mode='r', encoding='utf-8'):
#         # self.x = open(filepath, mode=mode, encoding=encoding)
#         self.filepath = filepath
#         self.mode = mode
#         self.encoding = encoding
#
#     def write(self, str1):
#         f = open(self.filepath, mode=self.mode, encoding=self.encoding)
#         t = time.strftime('%Y-%m-%d %X')
#         print(t)
#         print(self.filepath, self.mode, self.encoding, str1)
#         f.write('{} {} {}'.format(t, str1, '\n'))
#         f.close()
#



import time
class Open:
    def __init__(self, filepath, mode='r', encoding='utf-8'):
        self.x = open(filepath, mode=mode, encoding=encoding)
        self.filepath = filepath
        self.mode = mode
        self.encoding = encoding

    def write(self, str1):
        t = time.strftime('%Y-%m-%d %X')
        print(t)
        print(self.filepath, self.mode, self.encoding, str1)
        self.x.write('{} {} {}'.format(t, str1, '\n'))

    def __getattr__(self, item):
        return getattr(self.x, item)
#
#
# # f = Open('info.txt', 'a')
# # f.write('1111')
#
# f = Open('info.txt', 'r+ ')
# # print(f.__dict__)
# f.write('1111')
# # f = Open('info.txt', 'r')
# # print(f.read)
# # print(f.__dict__)
#
# res = f.read()
# print(res)
# # f1 = getattr(f, 'write')
# # f1('66666')
