class Foo:
    def __init__(self, name):
        self.name = name

    def __setattr__(self, key, value):
        print(key, value)
        self.__dict__[key] = value

    def __delattr__(self, item):
        print('======>', item)

    def __getattr__(self, item):
        print('********', item)
        return True

    def walk(self):
        print('%s is walking' % self.name)

f = Foo('tsy')
f.age = 18
print(f.__dict__)
# print(f.a)
# setattr(f, 'sex', 'male')
# print(f.__dict__)
# del f.age
# delattr(f, 'age')
# print(Foo.__dict__)
# delattr(Foo, 'walk')
# print(Foo.__dict__)
# # print(f.__dict__)