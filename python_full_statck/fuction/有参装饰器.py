#_*_coding:utf-8 _*_

'''

装饰器用法：在被装饰函数上方加一个@函数名

def timmer(func):
    def wrapper(*args, **kwargs)
        pass
    return wrapper

def auth(func):
    def f():
        认证功能1
        其他功能
        func()
        其他功能
        pass
    return f

@auth    #auth = auth(foo)
@timmer
#如果有两层装饰器，先执行靠近被装饰函数的一层
foo = timmer(foo)
然后在执行上一层
此时 foo = auth(timmer(foo))
def foo():
    print('from foo')
'''

print('hello')
def auth2(auth_type):
    def auth(func):
        def f(*args, **kwargs):
            print(auth_type)
            print(func)
            if auth_type == 'file':
                name = input('input your name:')
                passwd = input('input your password:')
                if name == 'tsy' and passwd == '123':
                    print('login successful')
                    res = func(*args, **kwargs)
                    return res
                else:
                    print('Password or accouunt wrong')
            elif auth_type == 'sql':
                print('Later')
            else:
                pass
        return f
    return auth


@auth2('file')  #index = auth(index)
def index():
    print('Welcome index page')

index()