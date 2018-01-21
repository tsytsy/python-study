'''
python中类是由type()产生的，一个类至少有三个要素,type也称为元类
1. 类名 class_name
2. 父类 bases
3. 属性（数据属性，函数属性）
也可以理解为一个类的定义也就是在做这三件事情，也即可以使用type来模拟类的定义过程
'''


class Foo(metaclass=type):
    pass

f = Foo()
print(f)
print(type(f))
print(type(Foo))

# def func():
#     print('from func')
#
#
# class_name = 'spam'
# bases = (object,)
# class_dict = {
#     'x': 1,
#     'func': func
# }
# s = type(class_name, bases, class_dict)
# print(s)
# print(s.__dict__)


