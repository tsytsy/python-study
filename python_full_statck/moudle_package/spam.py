#spam.py

print('from the spam.py')

money = 1000

def read1():
    print('spam moudle:', money)


def read2():
    print('spam moudle')
    read1()

def change():
    global money
    money = 0
    return money



