import re
'''
思路
1. 先找到最里层的括号，计算出相应的乘除和加减，找到后替换这个（）
'''
def muldiv(s):
    while True:
        s1 = re.search('-?\d+\.*\d*[*/]-?\d+\.*\d*', s)
        if s1:
            int1 = eval(s1.group())
            if isinstance(int1, float):
                int1 = round(int1, 3)
            if int1 > 0:
                s2 = re.sub('-?\d+\.*\d*[*/]-?\d+\.*\d*', '+' + str(int1), s, count=1)
            else:
                s2 = re.sub('-?\d+\.*\d*[*/]-?\d+\.*\d*', str(int1), s, count=1)
            s = s2
            # print(s2)
        else:
            return s

def f(s):
    s0 = re.sub('--', '+', s)
    s1 = re.sub('\++', '+', s)
    s2 = re.sub('\+-|-\+', '-', s1)
    # print('****', s2)
    return s2

def addsub(s):
    while True:
        s1 = re.search('-?\d+\.*\d*[+\-]-?\d+\.*\d*', s)
        if s1:
            int1 = eval(s1.group())
            s2 = re.sub('-?\d+\.*\d*[+\-]-?\d+\.*\d*', str(int1), s, count=1)
            s = s2
            # print(s2)
        else:
            return s

def divkh(s):
    s1 = s.replace('(', '')
    s2 = s1.replace(')', '')
    return s2

s ='(1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) -(-4*3)/ (16-3*2)))'
# s = '(-40/5)'
s= s.replace(' ', '')

# print(s)
while True:
    s0_obj = re.search('\(([^()]+)\)', s)
    if s0_obj:
        s0 = s0_obj.group() 
        s1 = muldiv(s0)
        print('s1---->', s1)
        s2 = f(s1)
        print('s2---->', s2)
        s3 = addsub(s2)
        print('s3---->', s3)
        s4 = divkh(s3)
        print('s4---->', s4)
        int1 = eval(s4)
        s5 = re.sub('\(([^()]+)\)', str(int1), s, count=1)
        s = s5
        print('----->', s5)
    else:
        print('s5---->', s5)
        break
