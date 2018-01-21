# def charCount(s):
#     digitalCount = 0
#     letterCount = 0
#     spaceCount = 0
#     otherCount = 0
#     for ch in s:
#         if ch.isdigit():
#             digitalCount += 1
#         elif ch.isalpha():
#             letterCount += 1
#         elif ch.isspace():
#             spaceCount += 1
#         else:
#             otherCount += 1
#
#     print('''
# 	digitalCount occour {0}
# 	letterCount occour {1}
# 	spaceCount occour {2}
# 	otherCount occour {3}
# 	'''.format(digitalCount, str(letterCount), spaceCount, otherCount))
#
#
# charCount('asd98008>>>/??')

# def charCount(s):
# 	#定义一个字典，将要用的key-value存在字典中
# 	res = {
# 		'digitalCount': 0,
# 		'letterCount': 0,
# 		'spaceCount': 0,
# 		'otherCount': 0
# 	}
# 	for ch in s:
# 		if ch.isdigit():
# 				res['digitalCount'] += 1
# 		elif ch.isalpha():
# 			res['letterCount'] += 1
# 		elif ch.isspace():
# 			res['spaceCount'] += 1
# 		else:
# 			res['otherCount'] += 1
# 	return res
#
#
# print(charCount('asda976>>/> vv sada'))
#
# from urllib.request import urlopen
# def get(url):
#     def index():
#         return urlopen(url).read()
#     return index
#
# f=get('http://www.python.org')
# print(f.__closure__[1].cell_contents)


# print(f())
# import os
#
# g = os.walk('D:\\a')
# path_list = []
# for i in g:
#     # print(i)
#     # print(i[2])
#     for j in range(len(i[2])):
#         # print(j)

#用函数思想来实现文件内容的过滤

# import os
# def search(file_path):
#     '''
#     :param path:需要查找的文件的路径
#     :return:
#     '''
#     g = os.walk(file_path)
#     path_list = []
#     for i in g:
#         for j in range(len(i[2])):
#             path_list.append(i[0] + '\\' + i[2][j])
#     return path_list
#
#
# def find(pattern, path_list):
#     path_list2 = []
#     for path in path_list:
#         with open(path, 'r') as f:
#             for line in f.readlines():
#                 if pattern in line:
#                     path_list2.append(path)
#                     break
#     return path_list2
#
# def printer(path_list):
#     for path in path_list:
#         print(path)
#
#
# printer(find('python', search(r'D:\a')))

# def my_tail(file_path):
#     '''
#     源源不断的取最后一行数据,生成器用来生成数据的，那么怎么样可以不断的生成数据呢？使用next(g)不断的取调用函数
#     函数不断的返回值，就可以不停的进行调用
#     :param file_path:
#     :return:
#     '''
#     with open(file_path, 'r', encoding='utf8') as f:
#         f.seek(0, 2)
#         while True:
#             line = f.readline()
#             if not line:
#                 continue
#             yield line
#
#
# def my_grep(pattern, line):
#     for lines in line:
#         if pattern in lines:    #next(g)
#             print(line)
#
# g = my_tail('cache.txt')
# my_grep('hello', g)

#协程函数
# def eater(name):
#     print('%s start to eater' % name)
#     food_list = []
#     while True:
#         food = yield food_list
#         print('%s eat %s' % (name, food))
#         food_list.append(food)
# a = eater('tsy')
#
# next(a)
# print(a.send('meat'))

#
#
# import os,time
# def init(func):
#     def wrapper(*args,**kwargs):
#         res=func(*args,**kwargs)
#         next(res)
#         return res
#     return wrapper
#
# #找到一个绝对路径，往下一个阶段发一个
# @init
# def search(target):
#     '找到文件的绝对路径'
#     while True:
#         dir_name=yield #dir_name='C:\\egon'
#         print('车间search开始生产产品：文件的绝对路径')
#         time.sleep(2)
#         g = os.walk(dir_name)
#         for i in g:
#             # print(i)
#             for j in i[-1]:
#                 file_path = '%s\\%s' % (i[0], j)
#                 target.send(file_path)
#
# @init
# def opener(target):
#     '打开文件，获取文件句柄'
#     while True:
#         file_path=yield
#         print('车间opener开始生产产品：文件句柄')
#         time.sleep(2)
#         with open(file_path) as f:
#             target.send((file_path,f))
#
# @init
# def cat(target):
#     '读取文件内容'
#     while True:
#         file_path,f=yield
#         print('车间cat开始生产产品：文件的一行内容')
#         time.sleep(2)
#         for line in f:
#             target.send((file_path,line))
#
# @init
# def grep(pattern,target):
#     '过滤一行内容中有无python'
#     while True:
#         file_path,line=yield
#         print('车间grep开始生产产品：包含python这一行内容的文件路径')
#         time.sleep(0.2)
#         if pattern in line:
#             target.send(file_path)
#
# @init
# def printer():
#     '打印文件路径'
#     while True:
#         file_path=yield
#         print('车间printer开始生产产品：得到最终的产品')
#         time.sleep(2)
#         print(file_path)
#
#
#
# g=search(opener(cat(grep('python',printer()))))
# # g.send(r'D:\a')
#
with open('info.txt', 'r', encoding='utf8') as f:
    res = [line.strip().split(',') for line in f]
    staff_info = [{'staff_id': i[0], 'name': i[1], 'age': int(i[2]), 'phone': i[3], 'dept': i[4],
                   'enroll_date': i[5]} for i in res]




#
# d = {'dept': 'IT', 'name': 'tsy'}
# where = ['dept', '==', 'IT']

print(staff_info)
d = [{'dept': 'IT', 'name': 'tsy'},{'dept': 'HR', 'name': 'tty'}]
print('====>', id(d[1]['dept']))
where = ['dept', '=', 'HR']
print('++++++++++++',id(where[2]))

for d2 in staff_info:
    if 'Alex Li' in d2.values():
        print('**********',id(d2['dept']))
# # L = list(filter(lambda x: eval(str(x[where[0]]) + where[1] + where[2]), staff_info))
# # print(bool(d[where[0]]+where[1]+where[2]))
# L = list(filter(lambda x: eval(str(x[where[0]]) + where[1] + str(where[2])), staff_info))
# L = list(filter(lambda x: eval(str(x[where[0]])+where[1]+where[2]), staff_info))
# def f(d):
#     return [where[0]] is where[2]
f1 = filter(lambda x: eval(x[where[0]] + '==' + where[2]), staff_info)
print(f1)
for i in f1:
    print('----',i)






