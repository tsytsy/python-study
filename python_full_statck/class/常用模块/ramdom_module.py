import random
'''
1. random.random()  产生一个0-1之间的随机随机数
2. random.unique(a, b)  取一个a,b之间的小数
2. random.ranint(a, b)  Return random integer in range [a, b], including both end points.
3. randrange(start, stop=None, step=1, _int=int)   Choose a random item from range(start, stop[, step]
4. choice(seq)  取出序列中的一个元素（元素可以为任何类型）
5. sample(seq, num) 取出序列中的两个元素组成一个列表 
'''

# print(random.random())
# print(random.randint(1, 2))     # 取到一个区间内的整数，包括头部和尾部
# print(random.randrange(1, 2))   # 取到一个不包括结尾的整数
# print(random.choice([1, 2, [12, 1, 2]]))
# print(random.sample([1, 2, ['1', '2', '3'], (1, 2, 3)], 2))
# print()

# 随机的五位包括字符和数字的验证码

# 字符串列表
# L = list(range(48,58))
# L1 = list(range(65,91))
# L2 = list(range(97, 123))
# L.extend(L2)
# L.extend(L2)
# str1 = ''
# for i in range(5):
#     str1 += chr(random.choice(L))
# print(str1)

# 方法二：

def v_code():
    s = ''
    for i in range(6):
        num = str(random.randint(0, 9))
        alf1 = chr(random.randint(65, 90))
        alf2 = chr(random.randint(97, 122))
        s += random.choice([num, alf1, alf2])
    return s

print(v_code())
