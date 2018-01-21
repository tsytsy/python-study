#集合# 天然去重
#关系测试
#无序
#sets不记录元素位置或者插入点。因此，sets不支持 indexing, slicing,
linux = {'tsy', 'tsj', 't1', 1, 2, 1}
python = {'tsy', 1, '666', 'qqq'}

#交集intersection

# print(linux)
# print(python)
# print(linux.intersection(python))
# print(linux & python)
# print(linux)
# print(python)


#差集different

# print(linux)
# print(python)
# print(linux.difference(python))
# print(linux - python)
# print(python-linux)
# print(linux)
# print(python)
# print(linux.symmetric_difference(python)) #两个集合中都不在的都打印


##并集union

# print(linux)
# print(python)
# print(linux.union(python))
# print(linux)
# print(python)
# print()

#增


# print(linux.add('txy'))
# print(linux)

#删

# print(linux.pop())          #随机删除一个元素

# print(linux.discard('tsy'))   #删除一个元素，如果不存在也不会报错
# print(linux.remove('tsy'))    #删除一个元素，如果改元素不存在，name会报错
# print(linux)




#改





#查

#
# for x in linux:
#     print(x)

#其他
# print(linux)
# print(python)
# print(linux.update(python))  #更新操作，python中存在的合并到linux中，且如果linux之前有的元素进行更新，次操作会改变linux的内容
#         #union的功能差不多，但是union不会修改linux的内容吗，只是求出一个并集而已
# print(linux)
# print(python)
# print()

x1 = list('tsyt')
print(x1)
x2 = dict()
print(x2)
x3 = set('tsyt')
print(x3)