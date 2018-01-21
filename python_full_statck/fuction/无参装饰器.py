#装饰器的存在主要是为了不修改原函数的代码，也不修改其他调用这个函数的代码，就能实现功能的拓展。
#开放封闭原则

import time
def timmer(func):
    def f(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        stop_time = time.time()
        print('running time is {}'.format(stop_time-start_time))
        return res
    return f

@timmer    #index = timmer(index)
def index():
    print('Welcome to happy-time')

@timmer
def auth(name, passwd):
    print(name, passwd)


@timmer
def my_max(x, y):
    res = x if x > y else y
    return res
index()
auth('tsy', '123')
# print(my_max(1, 2))