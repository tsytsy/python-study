# with open('info.txt', 'r', encoding='utf8') as f:
#     res = [line.strip().split(',') for line in f]
#     staff_info = [{'staff_id': i[0], 'name': i[1], 'age': int(i[2]), 'phone': i[3], 'dept': i[4],
#                    'enroll_date': i[5]} for i in res]
#
#
# L = [{'dept': 'IT', 'name': 'tsy'},{'dept': 'HR', 'name': 'tty'}]
#
# where = ['dept', '==', '"IT"']
# d = {'dept': '"IT"', 'name': 'tsy'}
# where1 = ["staff_id", "name", "age", "phone", "dept", "enroll_date", "=", ">=", "<=", ">", "<", "运维", "IT", "SA", "无"]
# def func(d1):
#     tiaojian = [d1[where[0]], where[1],where[2]]
#     print(tiaojian)
#     condition = eval(''.join(tiaojian))
#     print(condition)
# func(d)


from threading import Timer
import time
import datetime


def func(msg, starttime):
    print('程序启动时刻：', starttime, '当前时刻：', time.time(), '消息内容 --> %s' % (msg))


# # 下面的两个语句和上面的 scheduler 效果一样的
# Timer(5, func, ('hello', time.time())).start()
# Timer(3, func, ('world', time.time())).start()
print(datetime.datetime.now())
'''
s = sched.scheduler(time.time, time.sleep)
s.enter(delay, priority, func1, (arg1, arg2, ...))
s.enter(delay, priority, func2, (arg1, arg2, arg3, ...))
s.run()
'''