#抽象类是一个特殊的类，它的特殊之处在于只能被继承，不能被实例化
import abc


class All_file(metaclass=abc.ABCMeta):
    all_type = 'file'

    @abc.abstractmethod
    def read(self):
        pass

    @abc.abstractmethod
    def write(self):
        pass


class Txt(All_file): #文本，具体实现read和write
    def read(self):
        print('文本数据的读取方法')

    def write(self):
        print('文本数据的读取方法')


class Sata(All_file): #磁盘，具体实现read和write
    def read(self):
        print('硬盘数据的读取方法')

    def write(self):
        print('硬盘数据的读取方法')

class Process(All_file):
    def read(self):
        print('进程数据的读取方法')

    def write(self):
        print('进程数据的读取方法')


t1 = Txt()
t1.read()
print(t1.all_type)
t1.write()
s1 = Sata()
s1.write()
s1.read()
print(s1.all_type)
