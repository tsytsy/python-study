class Foo:
    money = 1

    def __init__(self):
        self.__x = 1

    def bar(self):      #将对象传给self
        print(self.__x)

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @staticmethod     #不用传参给第一个位置
    def func(num):
        if num:
            return True

    @classmethod
    def test(cls, y):   #将class传给第一个位置
        print('=======>')
        print(cls.money)
        print(y)

f= Foo()
# print(f.test)
# print(Foo.test)
# print(f.bar)
# print(Foo.bar)
# print(Foo.func)
# print(f.func)
print(f.__dict__)
print(f.x)
print(f.func(1))