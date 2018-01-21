def file_alter(file, old_content, new_content):
    str1 = ''
    with open(file, 'r') as f:
        for line in f:
            if old_content in line:
                line = line.replace(old_content, new_content)
            str1 += line

x = 1

def func():
    print('from func')
    x = 2
    a = 1
    b = 2
    # print(globals())
    # print(locals())


class Garen:
    'Garen class'
    __camp = 'Demacia'
    money = 1000
    n = 0

    def __init__(self, name, life_value=500, attack_value=59):
        self.name = name
        self.life_value = life_value
        self.attack_value = attack_value
        Garen.n += 1

    def attack(self, enemy):
        enemy.life_value -= self.attack_value

    def xianshi(self):
        print(self.name, self.life_value, self.attack_value, self.camp, self.money)

    # print('========', locals())
    # print(globals())


# func()
g1 = Garen('111')
print(g1.__dict__)
print(Garen.__dict__)
print(g1._Garen__camp)


# print(globals())
# print(Gaven.__dict__)
# print(g1.__dict__)
# print(g1.xianshi)
# g1.xianshi()
# print(globals())
# x = 1
# print(globals())