# class C:
#     def __init__(self):
#         print('init')
#
#     def __str__(self):
#         return 'hello'
#
#
# c = C()
# print('qqq'.__str__())
# print(c)


import time

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # @staticmethod
    # def now(cls): #用Date.now()的形式去产生实例,该实例用的是当前时间
    #     print(cls)
    #     t = time.localtime() #获取结构化的时间格式
    #     obj = cls(t.tm_year, t.tm_mon, t.tm_mday) #新建实例并且返回
    #     return obj
    #
    # @staticmethod
    # def tomorrow(cls):#用Date.tomorrow()的形式去产生实例,该实例用的是明天的时间
    #     t = time.localtime(time.time()+86400)
    #     return cls(t.tm_year, t.tm_mon, t.tm_mday)

    @classmethod
    def now(cls):  # 用Date.now()的形式去产生实例,该实例用的是当前时间
        print(cls)
        t = time.localtime()  # 获取结构化的时间格式
        obj = cls(t.tm_year, t.tm_mon, t.tm_mday)  # 新建实例并且返回
        print(obj)
        return obj

    @classmethod
    def tomorrow(cls):  # 用Date.tomorrow()的形式去产生实例,该实例用的是明天的时间
        t = time.localtime(time.time() + 86400)
        return cls(t.tm_year, t.tm_mon, t.tm_mday)


class EuroDate(Date):
    def __str__(self):
        return '年:%s,月:%s,日:%s' % (self.year, self.month, self.day)


e1 = EuroDate.now()
print(e1)