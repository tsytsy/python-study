#实参
# 1. 按关键字传值


# def foo(x, y):
#     print(x)
#     print(y)


# foo(2, 1)

#2. 按关键字传值
# foo(x=1, y=2)
# foo(y=2, x=1)

#3. 混着用

# foo(1, y=2)

#问题一：按位置传值必须在关键字传值的后面
# foo(x=1, 2)
#问题二：对于一个形参只能赋值一次
# foo(1, x=1)


#形参

#位置参数:必须传值的参数
# def foo(x, y):
#     print(x)
#     print(y)

#foo(1)
'''
默认参数
当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
使用默认参数有什么好处？最大的好处是能降低调用函数的难度。
'''

# def foo(x, y=1):
#     print(x)
#     print(y)

#*args


# def my_sum(*args):
#     print(args)
#     sum1 = 0
#     for i in args:
#         sum1 += i
#     return sum1
#
#
# print(my_sum(1, 2, 34))


#args与默认参数和位置参数混用,*args要放到位置参数后面，默认参数放最后
# def foo(x, *args):
#     print(x)
#     print(args)
#
# foo(1, 2, 3, 4)
print('start')
def auth(name, passwd, sex='male'):
    print(name)
    print(passwd)
    print(sex)


def foo(*args, **kwargs):
    auth(*args, **kwargs)

if __name__ == '__main__':
    foo('tsy', '123')