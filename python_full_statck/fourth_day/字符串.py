# _*_ coding:utf-8 _*_

name = 'TSY1 tsy tsy'
name1 = "    123123123abc"
# print(name.capitalize()) #首字母大写,其他位小写
# print(name.casefold())  #全部变成小写
# print(name.center(50, '*'))
# print(name.count('t', 3, 5))
# print(name.endswith('y'))
# print(name.expandtabs(30)) #设置tab的长度
print(name.find('tsy'))  #找到第一次出现的位置，返回索引值，找不到则返回-1
# print(name.index('tt'))  ##找到第一次出现的位置，返回索引值，找不到就报错
# print(name1.isalnum())
print('11'.isdecimal())    #判断字符里是否是一个十进制的正整数
print("aa".isalpha())      #字符串里只有字母
print('aaaaa1111'.upper())
print('Today Headline'.istitle()) #是否为标题，每个单词的首字母大写
print(''.join(['1', '2', '3']))  #将列表凭借为字符串,列表中的数据为字符串
print(name1.lstrip())
if "TSY" in name:
    print('hhhhhh')
print(name.replace('tsy', 'TAY'))
print(name)
