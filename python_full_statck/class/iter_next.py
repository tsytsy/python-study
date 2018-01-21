from collections import Iterable, Iterator

# class People:
#     y = 1
#     __slots__ = ['x', 'name', 'age', 'z']
#     # y = 1
#     def __init__(self, name):
#         self.name = name
#
#     def run(self):
#         print('from run')
#
# p = People('tsy')
# # print(p.__dict__)
# print(People.__dict__)
# # p.age = 18
# # print(p.__dict__)


# class People:
#
#     def __init__(self, start):
#         self.count = start
#
#     def run(self):
#         print('from run')
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.count += 1
#         if self.count == 10:
#             raise StopIteration
#         return self.count
#
#
# p = People(0)
# print(isinstance(p, Iterable))
# print(isinstance(p, Iterator))
# # print(next(p))
# # print(next(p))
# for i in p:
#     print(i)

class My_Range:
    def __init__(self, start, stop, step=1):
        self.start =start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        n = self.start
        if n > self.stop:
            raise StopIteration
        self.start += self.step
        return n

my_range = My_Range(0, 5, 3)
for i in my_range:
    print(i)