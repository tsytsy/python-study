import time
'''
时间模块
1. time.time(): Return the current time in seconds since the Epoch，用来给电脑看的时间
2. time.localtime():返回的是一个时间元祖，用来对时间进行操作的
3. time.strftime('%Y-%m-%d %X'):用来显示时间的，给人看的时间
'''
print(time.time())
print(time.localtime())
c = time.localtime()
print(c[0])
print(c.tm_year)

print(time.strftime('%Y/%m%d/%X'))
# C:\Users\jie\.PyCharmCE2017.2\system\python_stubs\969577316\time__module.py