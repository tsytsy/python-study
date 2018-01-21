#什么是闭包
'''
闭包：#闭包的意义：返回的函数对象，不仅仅是一个函数对象，在该函数外还包裹了一层作用域，这使得，该函数无论在何处调用，优先使用自己外层包裹的作用域
#闭包:内部函数包含对外部作用域而不是对全局作用域的名字的引用
#应用领域：延迟计算（原来我们是传参，现在我们是包起来）
'''

def waihanshu():
    x=1
    y=2
    def neihanshu(z):
        print('from neihanshu')
        print(x*y*z)
        return x, y
    return neihanshu


if __name__ == '__main__':
    f = waihanshu()
    k, v = f(2)