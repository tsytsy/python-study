'''
1. 什么是类？什么是对象？
2. 类是如何定义的:class
3. 类的属性：特征(变量)和方法(函数)
4. 如何引用类
5. 如何引用属性
'''






class Student:
    country = 'China'
    position = 'Student'

    def __init__(self, ID, NAME, SEX):
        self.id = ID
        self.name = NAME
        self.sex = SEX
        self.count = 0

    def search_score(self):
        print('tell score')
        return 123

    def study(self):
        print('%s is study' % self.name)

# def func():
#     print('from func')


# Student.method = func
#
# print(Student.__dict__)
# s1 = Student('1', 'tt', 'm')
# s2 = Student('2', 'ttt', 'm')
# print(s1.id, id(s1.id))
# print(s2.id, id(s2.id))
# print(s1.__dict__, s2.__dict__)
# print(s1.country, id(s1.country))
# print(s2.country, id(s2.country))
# print(Student.country, id(Student.country))
# print(s1.study,'\n', s2.study,'\n', Student.study)
# print(Student.method)
# s1.study()
# print()
# Student.study(s2)


# #实例化:实例化时候回条用方法__init__()
# s1 = Student('12312', 'tsy', 'male')
# # print(s1.search_score)
# # print(s1.study)
# # s2 = Student('12313', 'lyt', 'female')
# # #查
# # # print(s1.id, s2.id)
# # # print(s1.name, s2.name)
# # # print(s1.sex, s2.sex)
# # # print(s1.country, s2.country)
# # # print(s1.search_score(), s2.search_score())
# #
# # #增加
# print(s1.__dict__)
#
# # print()
# s1.x = 1
# # s2.x = 1
# # # x = 2
# # # print(s1.x)
# # # print(s2.x)
# print(s1.__dict__)
# #
# # #删除
# # # del s1.x
# # # print(s1.x)
# #
# #改
# # s1.id = '1111'
# # print(s1.id)
# # s1.country = 'aaa'
# # print(s1.country)
# # print(Student.country)
# '----------------------------------------------'
# #类的引用
#
# #查
# # print(Student.country)
# # print(Student.__init__)
# # print(Student.search_score)
# # print(Student.study)
# # print(Student.search_score(123))
# # # print(s1.id)
# # # Student.__init__(s1, '222', 'tsy', 'male')
# # # print(s1.id)
# #
# # #改
# print(s1.country)
# # Student.country = 'bbb'
# # print(s1.country)
#
#
# #
# # #增加
# print(Student.__dict__)
# Student.xx =999
# # print(Student.xx)
# # print(s1.xx)
# print(Student.__dict__)
#
# #删除
#
# # del Student.xx
# # print(Student.xx)
#
# # print(s1.study)
# # print(Student.study)



class txtfile:
    '''
    a.txt,b.txt,c.txt
    1. 文件类型都是txt
    2. 文件名字不一样
    3. 都具有增删改查方法
    '''
    file_type = '.txt'

    def __init__(self, file_name):
        self.file_name = file_name + '.txt'

    def file_append(self, app_content):
        with open(self.file_name, 'a') as f:
            f.write(app_content)

    def file_delete(self, del_content):
        str1 = ''
        with open(self.file_name, 'r') as f:
            for line in f:
                if del_content in line:
                    line = line.replace(del_content, '')
                str1 += line
        with open(self.file_name, 'w') as f:
            f.write(str1)

    def file_alter(self, old_content, new_content):
        str1 = ''
        with open(self.file_name, 'r') as f:
            for line in f:
                if old_content in line:
                    line = line.replace(old_content, new_content)
                str1 += line
        with open(self.file_name, 'w') as f:
            f.write(str1)

    def file_search(self):
        with open(self.file_name, 'r') as f:
            for line in f:
                print(line)


# file_obj = txtfile('info')
# print(file_obj.file_type)
# print(file_obj.file_name)
# file_obj.file_search()
# file_obj.file_append('lyt')
# file_obj.file_delete('lyt')
# file_obj.file_alter('500', 'tsj)
# file_obj.s1 = s1
# print(file_obj.s1)


'''
1. 创建两个英雄和一间装备，都是类
2. 英雄属性：名字，生命值，阵营，攻击力，技能
3. 装备属性：被动技能，增加攻击力，生命值，主动技能，攻击
'''

class Gaven:
    camp = 'Demacia'
    money = 1000
    n = 0

    def __init__(self, name, life_value=500, attack_value=59):
        self.name = name
        self.life_value = life_value
        self.attack_value = attack_value
        Gaven.n += 1

    def attack(self, enemy):
        enemy.life_value -= self.attack_value

    def xianshi(self):
        print(self.name, self.life_value, self.attack_value, self.camp, self.money)

class Riven:
    camp = 'Noxus'
    money = 1000

    def __init__(self, name, life_value=500, attack_value=52):
        self.name = name
        self.life_value = life_value
        self.attack_value = attack_value

    def attack(self, enemy):
        enemy.life_value -= self.attack_value

    def xianshi(self):
        print(self.name, self.life_value, self.attack_value, self.camp, self.money)


class blackcleaver:
    price = 425
    name = 'blackleaver'
    attack_value = 59
    life_value = 100

    def update(self, obj):
        obj.life_value += self.life_value
        obj.attack_value += self.attack_value
        obj.money -= self.price

    def fire(self, obj):
        obj.life_value -=1000

    def xianshi(self):
        print(self.price, self.name, self.attack_value, self.life_value)


b1 = blackcleaver()
r1 = Riven('666')
g1 = Gaven('111')
g1 = Gaven('222')
g1 = Gaven('333')
print(Gaven.n)
print(g1.n)

# # b1.xianshi()
# r1.xianshi()
# # g1.xianshi()
# # print(r1.__dict__)
# r1.b1 = b1
# # print(r1.__dict__)
# r1.b1.update(r1)
# r1.xianshi()
# g1.xianshi()
# r1.attack(g1)
# g1.xianshi()
# r1.b1.fire(g1)
# g1.xianshi()
# def func():
#     print('from func')
#
#
# print(r1.__dict__)
# r1.method = func
# print(r1.__dict__)
# r1.method()





