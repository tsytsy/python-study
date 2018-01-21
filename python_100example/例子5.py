#99乘法表
#1*1=1
#2*1=2,2*2=4
#3*1=3,3*2=6,3*3=9

for i in range(1, 10):
    for j in range(1, i+1):
        print("%d*%d = %2d" % (i, j, i*j), end=' ')
        if j == i:
            print('')