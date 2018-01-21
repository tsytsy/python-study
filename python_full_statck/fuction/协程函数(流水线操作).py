import time
import os


def init(func):
    def wrapper(*args, **kwargs):
        g = func(*args, **kwargs)
        next(g)
        return g
    return wrapper


@init
def search(target):
    '''
    :param path:需要查找的文件的路径
    :return:
    '''
    while True:
        file_path = yield
        g = os.walk(file_path)
        for i in g:
            for j in i[-1]:
                dir_name = ('%s\\%s' % (i[0], j))
                target.send(dir_name)


@init
def opener(target):
    while True:
        dir_name = yield
        with open(dir_name, 'r', encoding='utf8') as f:
            target.send((dir_name, f))


@init
def cat(target):
    while True:
        dir_name, f = yield
        line = f.read()
        target.send((dir_name, line))


@init
def grep(pattern, target):
    while True:
        dir_name, line = yield
        if pattern in line:
            target.send(dir_name)


@init
def printer():
    while True:
        dir_name = yield
        print(dir_name)


g = search(opener(cat(grep('python', printer()))))
g.send(r'D:\a')

