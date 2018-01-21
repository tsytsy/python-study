# class ParentClass1: #定义父类
#     pass
#
# class ParentClass2: #定义父类
#     pass
#
# class SubClass1(ParentClass1): #单继承，基类是ParentClass1，派生类是SubClass
#     pass
#
# class SubClass2(ParentClass1,ParentClass2): #python支持多继承，用逗号分隔开多个继承的类
#     pass
#
# print(SubClass1.__bases__)
# print(SubClass2.__bases__)
#
# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def walk(self):
#         print('%s is walking' % self.name)
#
#     def say(self):
#         print('%s is saying' % self.name)
#
# class People(Animal):
#     pass
#
# class Pig(Animal):
#     pass
#
# class Dog(Animal):
#     pass
#
# p1 = People('tsy',21)
# print(p1.name, p1.age)
# p1.walk()
# p1.say()


class Hero:
    money = 1000

    def __init__(self, name, life_value, attack_value):
        self.name = name
        self.life_value = life_value
        self.attack_value = attack_value
        print(self.name, self.life_value, self.attack_value, self.camp, self.money)

    def attack(self, enemy):
        enemy.life_value -= self.attack_value
        print('========>')

    def xianshi(self):
        print(self.name, self.life_value, self.attack_value, self.camp, self.money)


class Garen(Hero):
    camp = 'Demacia'

    def __init__(self, name, life_value, attack_value, stript):
        super().__init__(name, life_value, attack_value)
        self.stript = stript
        # print(self.name, self.life_value, self.attack_value, self.camp, self.money, self.stript)

    def attack(self, enemy):
        super().attack(enemy)
        print('from Garen')

    def fire(self, enemy):
        enemy.life_value -= 100


class Riven(Hero):
    camp = 'Noxus'


class equitment:

    def __init__(self, price, life_value, attack_value):
        self.price = price
        self.life_value = life_value
        self.attack_value = attack_value

    def update(self, obj):
        obj.money -= self.price
        obj.attack_value += self.attack_value
        obj.life_value += self.life_value


g1 = Garen('666', 400, 59, 'aaa')
r1 = Riven('777', 410, 61)
b1 = equitment(150, 100, 10)
g1.attack(r1)

# r1.b1 = b1
# r1.xianshi()
# r1.b1.update(r1)
# r1.xianshi()

# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.walk()
#         self.speak()
#
#     def walk(self):
#         print('{} is walking'.format(self.name))
#
#     def speak(self):
#         print('%s is speaking' % self.name)
#
#
# class People(Animal):
#
#     def think(self):
#         print('Peope can think')
#
#
# class dog(Animal):
#     pass
#
#
# class Chinese(People):
#     pass
#
# c = Chinese('tsy', 26)
# print(c.__dict__)
# c.think()
# # c.walk()
# # c.speak()
#
# class People:
#
#     def __init__(self, name, age, course):
#         self.name = name
#         self.age = age
#         self.course = course
#
#
# class Teacher(People):
#     def teach(self):
#         print('%s is teaching %s' % (self.name, self.course.name))
#
#
# class Student(People):
#     def study(self):
#         print('%s is studying %s' % (self.name, self.course.name))


# class Course:
#
#     def __init__(self, name, price, period):
#         self.name = name
#         self.price = price
#         self.period = period
#
#     def update(self):
#         print('%s is updating' % self.name)
#
#
# python = Course('python', 7000, '4m')
# s1 = Student('tsy', 26, python)
# t1 = Teacher('eggon', 36, python)
# print(t1.course.price)
# t1.teach()
# s1.study()


