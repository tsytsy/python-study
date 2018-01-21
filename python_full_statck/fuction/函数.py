# #函数声明
#
# def foo():
#     'declare a fuction'
#     print("hello")
#
#
# foo()
# res = foo()
# print(res)

#函数返回
# def bar(x, y):
#     res = x if x > y else y
#     return res
# res = bar(1,2)
# print(res)
# def foo(x, y):
#     return x, y
#
# k, v = foo(1, 2)
# # print(k, v)
# def foo(x, y=1, *args):
#     print(y)
#     print(args)
#
# foo(1,2,3)
#
# def print_line():
#     print("*"*10)
# print_line()
# def auth(name, passwd):
#     if name == 'tsy' and passwd == '123':
#         return True
#
#
# def auth(name, passwd):
#     pass
#
#
# auth('tsy', '123')

#
# def multi_value(x, y, z):
#     '''
#
#     :param x:返回一个value x
#     :param y:
#     :param z:
#     :return:
#     '''
#     return (1,2,3,4,5,6,[1,2],{'a':2},{1,2,3})
#
#
# p = multi_value(1, 2, 3)
#
# print(p)
#

# def my_sum(x, y=3, z=1):
#     '''
#     :param x:形参x只是一个没有值的变量，只有当函数调用时，x才会进行值的
#     绑定，当函数执行完之后，关系绑定结束
#     :param y:
#     :return:
#     '''
#     print(x)
#     print(y)
#     print(z)
#     return x+y
#
# my_sum(x=2)
'''
 位置参数和默认参数，且必选参数在前，默认参数在后，不然会出现歧义，定义默认参数要牢记一点：默认参数必须指向不变对象！
'''
# def power(x, n=2):

#     '''
#
#     :param x: a number
#     :param n:
#     :return:
#     '''
#     sum1 = 1
#     for i in range(n):
#         sum1 *= x
#     return sum1
#
# print(power(5))


#
'''
可变参数 *args
'''


# def squareRoot(*args):
#     '''
#
#     :param args:x*x+y*y+z*z.......
#     :return: Calculate the square root of several numbers
#     '''
#     sum1 = 0
#     for num in args:
#         sum1 += num*num
#     return sum1
#
#
# print(squareRoot(3, 4, 6))
#
# print(squareRoot(*[1, 2, 3]))

#关键字参数**argc

# def person(name, age, *argc, **kwargs):
#     '''
#
#     :param name:
#     :param age:
#     :param argc:
#     :param kwargs:
#     :return:
#     '''
#     print(name)
#     print(age)
#     print(argc)
#     print(kwargs)
#
# d1 = {'job':'python'}
# person('tsy', '25', 11111, 22222, job='python')
# person('tsy', '25', 11111, 22222, **d1)


# def person(x, y=1, *argc):
#     print(x)
#     print(argc)
#     print(y)
#
#
# person(1, 34, 1, 3, 4)

# def auth(name, passwd):
#     if name == 'tsy' and passwd == '123':
#         print('Welcome this party')
#
# auth("tsy", '123')

