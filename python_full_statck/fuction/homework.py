#1. 写函数，用户传入修改的文件名，与要修改的内容，执行函数，完成批了修改操作


# def modifyFileContent(file, old_content, new_content):
#     '''
#     文件的修改是需要重复覆盖的，不需要修改的内容保存下来，需要修改的内容找到后也保存下来，然后写到文件中
#     首先打开文件
#     找到文件位置，然后替换
#     :param file:文件名
#     :param old_content:旧内容
#     :param new_content:新内容
#     :return:None
#     '''
#     L = []
#     with open(file, 'r', encoding='utf8') as f:
#         for line in f.readlines():
#             if old_content in line:
#                 new_line = line.replace(old_content, new_content)
#                 L.append(new_line)
#             else:
#                 L.append(line)
#     print(L)
#     with open(file, 'w', encoding='utf8') as f:
#         for line in L:
#             f.write(line)
#     print(L)
#
# modifyFileContent('hello.txt', 'tsy', 'lyt')


#2、写函数，计算传入字符串中【数字】、【字母】、【空格] 以及 【其他】的个数


# def charCount(str1):
#     digtalCount = 0
#     letterCount = 0
#     spaceCount = 0
#     otherCharCount = 0
#     for char in str1:
#         if char.isdigit():
#             digtalCount += 1
#         elif char.isalpha():
#             letterCount += 1
#         elif char.isspace():
#             spaceCount += 1
#         else:
#             otherCharCount += 1
#     print(str1)
#     print('digtal count is >>>>', digtalCount)
#     print('letter count is >>>>', letterCount)
#     print('space count is >>>>', spaceCount)
#     print('other count is >>>>', otherCharCount)
#
#
# strInput = input('input your strings:')
# charCount(strInput)



#3、写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5

# def lengthObject(object1):
#     length = len(object1)
#     print('''
#         type:%s
#         length:%s
#         ''' % (len(object1), type(object1)))
#     if length > 5:
#         return True
#     else:
#         return False
#
#
# # object1 = [123, 1, {"name": 'tsy', 'age': 21}, [1, 2, 3]]
#
# object1 = (1, 2, (1, 2), {'1': 1, '2': 2})
# print(lengthObject(object1))


#4、写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
# def saveLengthList(L=None):
#     if len(L) > 2:
#         return L[0:2]
# print(saveLengthList(1))

#5、写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。
# def saveLengthList(L=None):
#     newL = []
#     for i in range(len(L)):
#         if not(i % 2 == 0):
#             newL.append(L[i])
#     return newL
#
#
# print(saveLengthList([1,2,3,4,5,6,7,8,9]))


#6、写函数，检查字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者

# d1 = {'1': [1, ],
#       '2': '123123123123',
#       '3': 'asdq'}
# def f(d):
#     d1 = {}
#     for key in d:
#         if len(d[key]) > 2:
#             d1[key] = d[key][0:2]
#         else:
#             d1[key] = d[key]
#     return d1
# print(f(d1))

def main():
    f1()
    f2()


def f1():
    print('from f1')
def f2():
    print('from f2')

main()
