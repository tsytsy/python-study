class C:
    x = 1

    def __init__(self, name):
        self.name = name

    def walk(self):
        print('from walk')

c = C('tsy')
print(c.name)