import time


class Open:
    def __init__(self, filepath, mode='r', encoding='utf-8'):
        self.x = open(filepath, mode=mode, encoding=encoding)
        self.filepath = filepath
        self.mode = mode
        self.encoding = encoding
        print(filepath, mode, encoding)

    def write(self, str1):
        t = time.strftime('%Y-%m-%d %X')
        # print(t)
        # print(self.filepath, self.mode, self.encoding, str1)
        self.x.write('{} {} {}'.format(t, str1, '\n'))

    def __enter__(self):
        print('enter')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.x.close()
        return 1

    def __del__(self):
        print('del')

    def __getattr__(self, item):
        return getattr(self.x, item)


# f = Open('info.txt', 'a')
# # del f
# print('================')
# time.sleep(5)
# print(f.__dict__)
# f.write('11111111')
# f.close()
with Open('info.txt', 'a') as f:   # Open进行实例化，with会进入类中的__enter__函数，将enter函数粉返回值给f
    print(f)
    f.write('66666')
    # raise NameError('no name')

print('========================')

