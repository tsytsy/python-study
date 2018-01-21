salaries = {
    'egon': 3000,
    'alex': 100000000,
    'wupeiqi': 10000,
    'yuanhao': 250
}


# def get_value(k):
#     return salaries[k]
#
# #匿名函数，不需要提供函数名，只返回一个表达式
# f = lambda k: salaries[k]
# print(f('alex'))
#
# print(max(salaries, key=lambda k: salaries[k]), max(salaries.values()))
#
# print(max([1,2], [3,1,2]))
# L = [1, 2, 3]
# s = 'hel'
# a = zip(L, s)
# print(a)
# for i in a:
#     print(i)

# print(max(zip(salaries.values(), salaries.keys())))
#匿名函数没有函数名，只有参数和表达式，返回的
# f = lambda x=1, y=2, z=2: x+y+z
# print(f)
#可迭代对象：[],(),{},generator,'',f,迭代器;  是一个序列

print(bool(0))
print(all('abcsda0'))
