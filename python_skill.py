# 1.切片操作
'''
当需要在列表或者元组或者字符串这些有序的对象中取得其中的一些子对象，应该使用切片功能
如在列表中取出奇数位的元素并且返回，如果使用for if 判断就会显得很麻烦
'''
#原始做法
def func(seq):
	L = []
	for i in range(len(seq)):
		if not(i % 2 == 0):
			L.append(seq[i])
	return L
#切片做法
def func2(seq):
	return seq[::2]
	#return seq[1::2]


#2. 利用字典来取代多个变量的赋值
'''
比如要计算一个字符串中的字母出现的个数、数字出现的个数、空格出现的个数以及其他出现的个数
'''
#原始做法
def charCount(s):
    digitalCount = 0
    letterCount = 0
    spaceCount = 0
    otherCount = 0
    for ch in s:
        if ch.isdigit():
            digitalCount += 1
        elif ch.isalpha():
            letterCount += 1
        elif ch.isspace():
            spaceCount += 1
        else:
            otherCount += 1

    print('''
	digitalCount occour {0}
	letterCount occour {1}
	spaceCount occour {2}
	otherCount occour {3}
	'''.format(digitalCount, letterCount, spaceCount, otherCount))
	#用format比用占位符要好些，因为%s是需要类型匹配的，但是format中的变量可以是任何类型的
	
#改进做法
def charCount(s):
	#定义一个字典，将要用的key-value存在字典中
	res = {
		'digitalCount': 0,
		'letterCount': 0,
		'spaceCount': 0,
		'otherCount': 0
	}
	for ch in s:
		if ch.isdigit():
				res['digitalCount'] += 1
		elif ch.isalpha():
			res['letterCount'] += 1
		elif ch.isspace():
			res['spaceCount'] += 1
		else:
			res['otherCount'] += 1
	return res
			
 #3. 在文件末尾，每增加一行，光标就指向下一行
 '''
 增加文件的内容时往往在最后一行加上新内容，此时用a+模式，不然内容会被覆盖
 a模式会在光标最后加上新增的内容，如果需要换行，只需要在内容后面加上一个换行符
 '''
 def file_append(file, content):
    with open(file, 'a') as f:
        f.write(content+'\n')
        print('add successful')
        f.flush()
        f.close()
 
 #4. 格式化输出format
 '''
 对输出的字符串有格式上的要求时，使用format函数可以很好的解决这个问题，比如输出的顺序问题，还有中文对其问题
 '''
 
 
 #5.值得注意的一件事是，在一个字符串中，行末的单独一个反斜杠表示字符串在下一行继
#续，而不是开始一个新的行。
 "This is the first sentence.\
This is the second sentence."

#6. 在python3中，input输入的都是一个在字符串，那么如何判断输入的是一个数字呢（浮点数or整数）
'''
a = input('>>:')有下列三种情况
1. 输入的是全数字(整数字符串)，如'1000',此时可以用a.isdigit()来判断
2. 输入的是浮点数，此时数字中带有小数点，a.isdigit()会判断为假
第一种思路是将输入变成float，如果是数字那么就变成了浮点数，但是如果不是上面的两种情况，就会报错，出现异常
比如输入的是'ttt'，使用try except来判断就好
'''
def isnum(aString):
	try:
		float(aString)   #如果能用float进行装换的就是数字，返回True，如果出现错误，那么久跳到except,表明不是数字
		return True
	except:
		return False
		

#7. 对于输入input的判断

welcome = '''
	1. 取款
	2. 存款
	3. 转账
	4. 查询
	5. 账单

'''
while True:
	choice = input('>>input your number:')
	if choice == 'q':
		exit()
	elif choice not in ['1', '2', '3', '4', '5']:
		continue
	break
	#choice 在列表中，根据choice找到对应的操作。 

#8. 自定义数据类型
'''
1. 基于继承的原理来定义自己的数据类型：继承标准类型，使用super()函数来继承
'''
class List(list):
    def __init__(self, L):
        if not isinstance(L, Iterable):
            raise ValueError('argument must be a iterable')
        for i in L:
            if not isinstance(i, int):
                raise ValueError('element must be int')
            self.append(i)

    def append(self, value):
        if not isinstance(value, int):
            raise ValueError('value must be int')
        super(List, self).append(value)

    def insert(self, index, value):
        if not isinstance(index, int):
            raise TypeError('must be int')
        if not isinstance(value, int):
            raise TypeError('must be int')
        super().insert(index, value)
'''
授权
'''

#获取文件夹大小
import os
from os.path import join, getsize
def getdirsize(dir):
    size = 0
    for root, dirs, files in os.walk(dir):
        size += sum([getsize(join(root, name)) for name in files])
    return size

if __name__ == '__main__':
    filesize = getdirsize(r'D:\workplace\python-study\python_full_statck\homework\FTPServer\home\tsy')
    print('There are %.3f' % (filesize / 1024 / 1024 ), 'Mbytes in E:\\chengd')
