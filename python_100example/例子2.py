#题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？

import math

# print(type(math.sqrt(21 + 100)) is int and type(math.sqrt(21 + 168) is int))
#
# x1 = str(math.sqrt(21 + 100)).split(".")[1]
# print(x1)
# x2 = str(math.sqrt(21 + 168)).split(".")[1]
# print(type(x2))

x = 0
while True:
    if int(str(math.sqrt(x + 100)).split(".")[1]) == 0 and int(str(math.sqrt(x + 168)).split(".")[1]) == 0:
        print(x)

    x += 1
    if x == 10000:
        break