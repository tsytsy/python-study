#练习一
from collections import Iterable
class List:
    def __init__(self, x):
        if not isinstance(x, Iterable):
            raise TypeError('argument must be iterable')
        for i in x:
            if not isinstance(i, str):
                raise TypeError('elenment must be a str')
        self.seq = list(x)
        # print(self.seq)

    def append(self, value):
        if not isinstance(value, str):
            raise TypeError('elenment must be a str')
        self.seq.append(value)

    def __str__(self):
        return str(self.seq)

    def __getattr__(self, item):
        # if not isinstance(item, str):
            # raise TypeError('elenment must be a str')
        return getattr(self.seq, item)


l = List(('1', '2'))
l.append('3')
print(l)
l.insert(0, 1)
print(l)
