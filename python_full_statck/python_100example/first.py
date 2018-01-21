# -*- coding: UTF-8 -*-

#有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
d = []
for j in range(1,5):
    for k in range(1,5):
        for l in range(1,5):
            if j!=k and j!=l and k!=l:
                d.append(int(str(j)+str(k)+str(l)))
print(d)
print(len(d))


print('a', end=' '),
print('b')
