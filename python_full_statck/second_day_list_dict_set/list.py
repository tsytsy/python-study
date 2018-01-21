
# -*- coding: UTF-8 -*-


# name1 = 'I love you'
# print(name1.replace('I', 'he'))
#
# print(name1)

name = ["tsy", "lyt", "tsj", "tsr", "t1", '4', '5', [1, 2, 3]]

#
# #增
# name.append(111)
# print(name)
# name.insert(2, "t1")
# print(name)
# name.extend(["t2", "t3"])
# print(name)
#name1 = ['aaa', 'bbb']
#name = name + name1
#print(name)

# print('************************')
# #删
# print(name.pop())
# print(name)
#
# name.remove("t2")
# print(name)
#print(name)
#name.clear()
#del name
# print(name.pop(-1))
# print(name)

#改,找到列表中是否存在这个元素，存在找到索引位置，并且修改
#
# print("************************")
#
# if "tsy" in name:
#     print(" 'tsy' index is " , name.index("tsy"))
#     # name[0] = 'tfy'
# else:
#     print("these is no 'tsy' in the name list")
#
#
# #查
# print("**************************")
#
# name.index('tsy')  #查索引位置
# name.count('tsy')  #查项目出现次数
# len(name)   #查列表长度
# print(name[3])         #访问列表中第4个值
# print(name[1:3])       #访问列表中从第2个到第3个的值
# print(name[-1])        #访问列表中的最后一个值
# print(name[:-2])       #访问列表中的所有值，但是把倒数第二个及后面的所有值都去掉
# print(name[-3:])       #访问列表中倒数第一个到倒数第三个的值
# print(name[0], name[3])    #注意取多个值的时候，不能直接把下标写到一起，需要按照这种方式写
# print(name[::2])       #打印列表，但是以2为步长，就是跳着切，也可以根据需求把这个步长给改了
# print(name)


# 排序,反转
# print(name)
# name.reverse()
# print(name)
# name.sort()
# print(name)
#
# name1 = name.copy()
# print(name1)
# print(id(name))
# print(id(name1))

#列表是一个容器，可以用来存储数据，可以很方便的对列表中的数据进行读写，查找等操作（增删改查）。


#列表copy
# name1=name.copy()
# # print(name, name1)
# print(name is name1)
#
#
# print(id(name))
# print(id(name1))
# name[1] = 't1'
# print(name)
# # print(name1)
# name2 = name[:]
# name[1] = '1'
# name[-1][0] = 'ttt'
# name3 = name[-1]
# print(name)
# print(name2)
# print(name3)
#
# name3.append('tty')
# print(name)
# print(name2)
# print(name3)


d = {1: {'1':6, '2': 'sada'}, 2: '2'}
print(type(d[1]))
print(type(d[2]))