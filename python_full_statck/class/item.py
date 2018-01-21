class Foo:
    def __init__(self, name):
        self.name = name

    '''
    实例在设置属性的方法通常有两种，第一种是通过'.'的形式去设置，如f.age = 18
    第二种是通过setattr,delattr这种形式去设置，但是这两种形式的本质都是要去执行对象的内置函数
    __setattr__()和__delattr()__，而对象属性的操作就是在对对象__dict__字典的操作。
    以下三个函数是对象在调用
    '''

    def __setattr__(self, key, value):
        # print('set attr')
        # print(key, value)
        # setattr(self, key, value)  # 触发递归，setattr使用的也是这个函数
        self.__dict__[key] = value

    def __delattr__(self, item):
        # print('del attr')
        # raise TypeError('element cannot delete')
        self.__dict__.pop(item)

    # 只有调用对象没有的属性才会触发这个函数
    def __getattr__(self, item):
        print('get attr')


    '''
    item系列的属性操作使得对象可以像字典一样，使用[]对属性进行操作，如
    __getitem__(self, item)获取属性的值f['name'],类似于f.name
    __setitem__(self, key, value)获取属性的值f['age'] = 18,类似于f.age = 18
    __delitem__(self, key)删除属性
    '''
    def __getitem__(self, item):
        print('get item')
        print(type(item))
        return self.__dict__[item]

    def __setitem__(self, key, value):
        print('set item')
        # self.__dict__[key] = value
        setattr(self, key, value)

    def __delitem__(self, key):
        print('del item')
        delattr(self, key)


f = Foo('tsy')
# print(f.name)
setattr(f, 'age', 21)
print(f.__dict__)
delattr(f, 'age')
print(f.__dict__)
f.xxxx

# f = Foo('tsy')
# print(f.__dict__)
# print(f.name)
# print(f.__dict__)
# print(f['name'])
# f['age'] = 19
# print(f['age'])
# del f['age']
# print(f.__dict__)
