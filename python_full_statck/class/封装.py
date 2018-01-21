#在python中用双下划线开头的方式将属性隐藏起来（设置成私有的）


#其实这仅仅这是一种变形操作
#类中所有双下划线开头的名称如__x都会自动变形成：_类名__x的形式：

# class A:
#     __N = 0             #类的数据属性就应该是共享的,但是语法上是可以把类的数据属性设置成私有的如__N,会变形为_A__N
#
#     def __init__(self):
#         self.__X = 10     #变形为self._A__X
#
#     def __foo(self):    #变形为_A__foo
#         print('from A')
#
#     def bar(self):
#         self.__foo()     #只有在类内部才可以通过__foo的形式访问到.
#
# #A._A__N是可以访问到的，即这种操作并不是严格意义上的限制外部访问，仅仅只是一种语法意义上的变形
#
# a = A()
# print(a.__dict__)
# a._A__foo()


# class A:
#     def fa(self):
#         print('from A')
#
#     def test(self):
#         self.fa()
#
#
# class B(A):
#     def fa(self):
#         print('from B')
#
#
# b = B()
# b.test() #b.test-->B--->A b.fa()


# class A:
#     def __init__(self, x):
#         self.__x = x
#
#     def tell(self):
#         print(self.__x)
#
#
# a = A(1)
# print(a.__dict__)
# # print(a.__x)
#
# a.tell()

#
# class B:
#     pass
#
# # B.__x=1
# # print(B.__dict__)
# # print(B.__x)
#
# b = B()
# b.__x = 1
# print(b.__dict__)
# print(b.__x)


# class A:
#     def __fa(self):     #在定义时就变形为_A__fa
#         print('from A')
#     def test(self):
#         self.__fa()      #只会与自己所在的类为准,即调用_A__fa
#
# class B(A):
#     def __fa(self):  #_B__fa
#         print('from B')
#
# b = B()
# b.test()
#
# class Teacher:
#     def __init__(self,name,age):
#         self.__name=name
#         self.__age=age
#
#     def tell_info(self):
#         print('姓名:%s,年龄:%s' %(self.__name,self.__age))
#
#     def set_info(self,name,age):
#         if not isinstance(name,str):
#             raise TypeError('姓名必须是字符串类型')
#         if not isinstance(age,int):
#             raise TypeError('年龄必须是整型')
#         self.__name=name
#         self.__age=age
#
# t1 = Teacher('eggon', 28)
#
# print(t1.__dict__)
# print(t1._Teacher__name)

# t=Teacher('egon',18)
# t.tell_info()
#
# t.set_info('egon',19)
# t.tell_info()


class A:
    '''
    __定义的时候变成_类名__变量
    _N  _A__N
    self.__name    self._A__name
    '''
    _N = 0

    def __init__(self, name, age):
        '''
        self.__name    self._A__name
        self.__age     self._A__age
        '''
        self._name = name
        self.__age = age

    def tell_info(self):
        print('name is %s' % self._name)
        print('age is %s' % self.__age)


a = A('tsy', 21)
print(a._name)
print(a.__dict__)
a.tell_info()