#字典-------->键值对key:value,key必须唯一
#无序性
#key是不可变的，value是可修改的
#字典删除最好在key后面加一个None,如果ke不存在，那么会引起错误，加上None则不会

#在字典中查找内容时使用name[key]程序出错，因为这个key不一定存在,程序跳出，此时
#最好使用in方法来超找是否存在这个key，存在返回1，不存在返回0 key in name;
#
# name = {110: ['tsy', 'red', 'rain'], 112: ['tsj', 'red', 'sun'],
#         113: ['lyt', 'pink', 'sun'],
#         't1': 'hhh', 't2': 'kkk', 118: 'rain from name'}
#
# dict2 = {118: 'rain',
#          119: 'hello'}
# print(name[110][0])

#增
# name[114] = ['tsr', 'red', 'sun']
# print(name)
# name1 = {'t1': 'kkk', 't2': '1111'}
# print(name.update(name1))



#删
# print(name.pop(112))
# print(name)
# print(name.pop(117, None)) #字典删除最好在key后面加一个None,如果ke不存在，那么会引起错误，加上None则不会
# print(name)
# del name[110]
# print(name)

#改
# name[110].append('111')
# print(name)
# name.setdefault()


#查
# print(name)
# # print(name[111])  #程序出错，因为这个key不一定存在
# print(name.get(111))
#
# print(111 in name)
# # if 111 in name:
# #     print("1111")
# # else:
# #     print("00000000")



#loop

# for i in name:
#     # print(i)     #只打印了key
#     print(i, name[i])

# for i in name.items():  #打印出了key和value，效率低，不用
#     print(i)

# print(name.keys())
# print(name.values())
# name.update(dict2)
# print(name)
# for i in name:
#     print(i, name[i][0])
# print("I am %d years old, %s" %(20, "hello"))
# # print(name[110])

info = {}
info = info.fromkeys([1, 2, 3])#将列表中的直作为key，初始化一个字典
info.update({1: "tsy", 2: 'tsj', 5: "tsr"})
print(info)

