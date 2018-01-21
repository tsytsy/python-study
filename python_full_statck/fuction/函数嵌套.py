#_*_ coding:utf-8 _*_

#命名空间
# '''
# 名称空间分为三种：内置名称空间、全局名称空间、局部名称空间
# 内置名称空间在解释中定义，也就是内置名称在解释器启动就存在了，比如一些内置函数在
# 解释器启动就可以直接调用
#
# 全局名称空间：在全局中定义的，可以在局部中使用
#
# 局部名称空间：在局部中定义的（如在函数中），不能再全局中使用
# '''
#
# x = 1
# def foo():
#     print('from foo')
#     y = 2
#     print(y)
#
#
# print(x)
# print(globals())
# print(locals())



#函数可以被当成变量，可以被赋值
# def foo():
#     print('from foo')
#
#
# print(foo)
# print(foo())

#把函数当成元素

#把函数当做容器类型的元素去用
#还记得我们用函数对象的概念，制作一个函数字典的操作吗，来来来，我们有更高大上的做法，在文件开头声明一个空字典，然后在每个函数前加上装饰器，完成自动添加到字典的操作

d = {}

def addtodict(func):
    def wrapper(*args, **kwargs):
        d[func.__name__] = func
        # print(d)
        func(*args, **kwargs)
    return wrapper
#
#
@addtodict
def add():
    print('=============== fuction add')


add()

# print(add.__name__)

def delete():
    print('================ fuct delete')


def modeify():
    print('================= fuction modify')


def search():
    print('================== fuction search')


def tell_cmd():
    msg = '''
    search  查询
    add     增加
    modify  修改
    delete  删除
    '''
    print(msg)



# dic1 = {
#     'search': search,
#     'add': add,
#     'delete': delete,
#     'modify': modeify
# }
#
# while True:
#     tell_cmd()
#     choice = input('input your choice>>>:'.strip())
#     print(choice)
#     dic1[choice]()




