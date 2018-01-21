##题目：输入三个整数x,y,z，请把这三个数由小到大输出。
import math
a = []
count = int(input('your conut'))
for i in range(count):
    a.append(int(input("input a number:")))
a.sort()
print(a)
print(max(a))