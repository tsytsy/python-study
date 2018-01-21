#spam.py
'''
11111
'''
print('from the spam.py')

money = 1000

# __all__ = ['money', 'read1']
def read1():
    print('spam moudle:', money)


def read2():
    print('spam moudle')
    read1()

def change():
    global money
    money = 0
    return money

class Foo:
    def __init__(self, name):
        self.name = name

    def run(self):
        print('%s is running' % self.name)

print(__name__)

if __name__ == '__main__':
    print(globals())
    read1()

if __name__ == 'spam':
    print('I has been a module')


