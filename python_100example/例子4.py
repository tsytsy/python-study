#题目：斐波那契数列。
#程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。


f = [0, 1]
count = 2
while True:
    f.append(f[count-1] + f[count-2])
    count += 1
    if count == 10:
        break

print(f)