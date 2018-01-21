
'''
1. 为什么要使用对象？什么是对象？
2. 对象在定义阶段就会去执行类数据和类方法，故类在定义阶段就可以知道类的__dict__()属性
3. .:专门用来访问属性，本质操作的就是__dict__
4. 一个类中可以分为三个部分：类数据属性，__init__,以及类函数，类类进行实例化时，首先会去运行_init__函数进行初始化
    然后得到一个实例的名字空间，这个函数一般是用来传输对象的不同属性的，即__dict__,当一个实例去调用类的数据属性时，
    访问的是类的数据指针，所有实例指向的都是一个内存地址。虽然对象在名字空间中(__dict__)没有函数名的存在，但是实际情况
    是类的函数属性绑定到了实例中，每一个实例都有不同的绑定函数地址。
5. 什么是继承?继承的作用是什么?
6. 什么是多态?多态的作用是什么?如何理解多态？
    多态在我看来就是父类中的函数在子类中重写，调用子类的函数时，不同的子类表现形式不同，如Animal的子类Dog
    和Cat，都继承了Animal的run属性，但是在两个子类中重新定义了run属性，这就使得在子类调用run属性的时候
    表现的行为不一样，称之为多态。多态的真正厉害之处在于，定义一个函数run()（比如len），其参数为父类Animal，
    所有的子类都有自己的run()函数，所以
    def run(obj = Animal())
        obj.run()
    不同的子类表现的行为呈现多种形态。
    举一个形象的例子。cat,dog,pig等都是动物，都从animal中继承了run的动作，当向全体动物发出一个run的指令
    时，所有的动物都run，但是跑步的形态和快慢都不一样，这就是多态。
7. 什么是派生？如何理解派生？
    子类继承父类时，继承了父类的所有属性，包括数据属性和函数属性。但是子类毕竟和父类不一样，子类有自己的心功能
    比如Cat()相对于Animal类来说，其自己本身的一个特性为吃鱼。那么此时Cat类中的fisheat()称为派生，子类派生
    出新的属性成为派生。
    子类有新的属性称为派生，子类属性变更称为多态。
8. 封装并不是单纯的隐藏数据。隐藏数据不是关键。关键是对数据做一定的保护措施。不是谁都可以改变数据。
    将数据隐藏起来这不是目的。隐藏起来然后对外提供操作该数据的接口，然后我们可以在接口附加上对该数据操作的限制，
    以此完成对数据属性操作的严格控制。打个比方，比如注册了支付宝账号，注册后，你有名称，邮箱，余额等等信息，
    名称和邮箱你自己可以改变，但是你的余额自己是改变不了的，只有充钱了，支付宝中的余额才会改变，也就是说，
    如果余额不经过封装，任何用户都是有权利改变这个数据属性的，但是经过封装后，这个数据属性就有了操作限制。这
    就是封装。
9. property:提供一种对将函数属性转变为数据属性的类型。比如说一个园的面积和周长，对于一个元来讲这两个参数
    都是属性。但是这两个参数是需要经过计算才能得出的。property很好的解决了这一个问题，让用户感觉到这两个
    参数都是数据属性，其实他们内部都是函数属性。property更为重要的应用就是，一个实例的属性一般都是私有属性
    不让外部去胡乱改变的，但是可以提供接口get和set去进行属性操作，这个时候我们就可以将这个数据属性的名称
    作为函数名称，然后使用property，将函数属性变为数据属性，此时就可以对数据增进行读写，改变，删除等。
10. 类中函数属性分为两种：绑定方法和非绑定方法。其中绑定发放又分为对象绑定方法和类绑定方法，类绑定方法要用
    @classmethod进行修饰，而对象绑定方法不需要任何的装饰器进行修饰（property不算）。绑定方法的第一个会自动的进行传值。
    非绑定方法是一个普通的函数，需要用@staticmethod进行修饰
11. 反射：通过字符串的形式操作对象相关的属性。hasattr(),getattr(),setattr(),delattr()
    这四个内置函数可以用来对属性进行增删改查。那为什么不直接用.的形式来对属性进行访问呢?.的方法只是操作已经知道
    的属性，对于不确定的属性并不知道。hasattr可以检查属性是否存在，但是.方法不能检查属性是否存在。
12. __setattr__, __delattr__,__getattr__:这三个函数是.方法和setattr()反射方法的内在方法，也就是说
    其他的对于属性的方法操作实际上是在对上诉三个函数的操作。如果重写这三个函数，会对所有的属性操作造成影响。
    当然如果确实需要对所有的赋值操作进行限制，那么久需要重写这写函数。任何对属性的操作都是在对__dict__字典
    进行操作，包括.方法，反射方法以及__setattr__方法。需要注意的是__getattr__()。属性不存在的时候才运行
    一个重要的运用是在定制自己的数据类型。如果自己定制的类没有改写python提供的函数，那么久去运行python提供的
    函数。
13. 定义自己的数据类型：原则是通过python提供的方法定义自己的数据类型。
14. __setitem__,__getitem,__delitem__。属性可以使用[]进行获得,本质上也是对字典__dict__进行操作
15. __str__:当使用内置函数print进行显示打印操作时，如print(obj),实际上调用的是obj.__str__()。所以如果需要对一个
    实例进行打印时，可以重写这个__str__()函数，此时print(obj)就是在执行__str__()函数。
16. __slot__字典会限制实例的属性，且实例没有__dict__字典，这种情形适用于有大量的实例要进行初始化，由于没有dict，所以
    保证没有dict字典占用内存。
17. __iter__和__next__：如果一个对象有__iter__()函数，说明这个对象是一个可迭代的对象；如果一个对象有__next__()
    函数，说明这个对象是一个迭代器
18. __del__析构方法，当对象在内存中被释放时，自动触发执行。如果产生的对象仅仅只是python程序级别的（用户级），那么无需
    定义__del__,如果产生的对象的同时还会向操作系统发起系统调用，即一个对象有用户级与内核级两种资源，比如（打开一个文件，
    创建一个数据库链接），则必须在清除对象的同时回收系统资源，这就用到了__del__
'''
# class Foo:
#     'Foo class'
#     x = 1
#
#     def __init__(self, name):
#         self.name = name
#
#     @staticmethod
#     def run():
#         print('running')
#
#     @classmethod
#     def now(cls):
#         y = cls('lyt')
#         return y.name
#
#     def study(self):
#         print('%s from study' % self.name)
#
#     def __call__(self, *args, **kwargs):
#         print('callable')
#
# class Bar(Foo):
#     def walk(self):
#         print('from walk')
#
#
# print(callable(Foo))
# print(Bar.__dict__)
# b = Bar('lll')


# print(Foo.__dict__)
# # f = Foo('tsy')
# f = Foo('tsy')
# print(f.__dict__)
# f.study()
# # f()
# # print(callable(f))
# # print(callable(Foo))
# print(f.run())
# print(Foo.now())
# print(f.now())

#
# class Foo:
#     def __fa(self):
#         print('from Foo')
#
#     def test(self):
#         self.__fa()
#
#
# class foo(Foo):
#     def __fa(self):
#         print('from foo')
#
# print(foo.__dict__)
# print(Foo.__dict__)
# f = foo()
# f.test()

# 封装，property
# class Foo:
#     def __init__(self, name, balance=0):
#         self.name = name
#         self.__balance = balance
#
#     @property
#     def balance(self):
#         return self.__balance
#
#     @balance.setter
#     def balance(self, value):
#         if not isinstance(value, int):
#             raise TypeError('must be int')
#         self.__balance += value
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('=============>')
#         return True
#
#
# f = Foo('tsy')
# print(Foo.__dict__)
# print(f.__dict__)
# print(f.balance)
# f.balance = '10000'
# print(f.balance)

# 反射
class Foo:
    x = 1
    __slots__ = ['z', 'y', 'name', 'age']   # 限制实例的属性

    def __init__(self, name):
        self.name = name

    def run(self):
        print('%s is runnung' % self.name)

    def __getitem__(self, item):
        return self.__dict__[item]
    #
    def __setitem__(self, key, value):
        self.__dict__[key] = value

    # def __str__(self):
    #     print('print函数会执行__str__模块')
    #     return self


    # def __setattr__(self, key, value):
    #     print('set attr')
    #     self.__dict__[key] = value
    #
    # def __getattr__(self, item):
    #     print('item no exits'
# print(Foo.__dict__)
# f = Foo('tsy')
# # print(f.__dict__)  # __slot__表明这个类型的实例没有dict字典，也就是这个类型的实例在__slot__字典里面
# f.score = 99

# print(f.__dict__)
# if hasattr(f, 'name'):
#     name = getattr(f, 'name')
# print(name)
# # print(hasattr(Foo, 'run'))
# # print(hasattr(Foo, 'x'))
# # print(hasattr(f, 'x'))
# # print(hasattr(f, 'run'))
# setattr(f, 'age', 21)
# setattr(f, 'sex', 'male')
# print(f.__dict__)
# delattr(f, 'age')
# print(f.__dict__)
# # print(f.name)
# print(getattr(f, 'name'))

class My_range:
    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        n = self.start
        self.start += self.step
        if n >= self.end:
            raise StopIteration
        return n


r1 = My_range(0, 9, 1)
# for i in r1:
#     print(i)
from spam import Foo

# print(hasattr(spam, 'Foo'))
f = Foo('tsy')
print(Foo.__module__)
print(My_range.__module__)
print(f.__class__)
print(r1.__class__)



