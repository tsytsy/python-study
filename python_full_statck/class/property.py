'property是一种特殊的属性，访问它时会执行一段功能（函数）然后返回值'
# import math
#
# class Circle:
#     def __init__(self, r):
#         self.r = r
#
#     @property     #area = property(area)
#     def area(self):
#         return math.pi * self.r**2
#
#     @property
#     def zhouchang(self):
#         return math.pi*2*self.r
#
#
# c = Circle(4)
# print(c.r)
# print(c.area)
# print(c.zhouchang)
#
# class People:
#     def __init__(self, name, age, sex):
#         self.__name = name
#         self.__age = age
#         self.__sex = sex
#
#     @property       #sex = property(sex)
#     def sex(self):
#         return self.__sex
#
#     # def change_sex(self, value):
#     #     self.__sex = value
#
#     @sex.setter
#     def sex(self, value):
#         self.__sex = value
#
#
# p1 = People('eggon', 21, 'male')
# # print(p1.__dict__)
# print(p1.sex)
# # p1.change_sex('female')
# # print(p1.sex)


class People:
    def __init__(self, name, sex):
        self.name = name
        self.__sex = sex

    @property
    def sex(self):
        return self.__sex

    @sex.setter
    def sex(self, value):   # = 触发改函数执行
        if value not in ['male', 'female']:
            raise ValueError('sex is wrong')
        self.__sex = value

    @sex.deleter
    def sex(self):      # del 触发改函数执行
        raise ValueError('sex cannot delete')


p1 = People('eggon', 'male')


# print(p1.__dict__)
print(p1.sex)
p1.sex = 'female'
print(p1.sex)
del p1.sex
# print(p1.sex)