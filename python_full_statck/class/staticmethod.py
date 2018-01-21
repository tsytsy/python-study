import time
'''
staticmethod

'''
class Data:
    def __init__(self, year, mon, day):
        self.year = year
        self.mon = mon
        self.day = day


    # def now(self):
        # t = Data(time.localtime()
    @staticmethod
    def now():
        t = Data(*time.localtime()[:3])
        print(t.year, t.mon, t.day)

Data.now()
a = Data(2018, 2, 3)
print(a.year, a.mon, a.day)
a.now()