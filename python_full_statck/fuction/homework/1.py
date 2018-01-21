# # d = {
# #     'staff_id': '1',
# #     'name': '1',
# #     'age': '1',
# #     'phone': '1',
# #     'dept': '1',
# #     'enroll_date': '1'
# # }
# # str1 = '{staff_id},{name},{age},{phone},{dept},{enroll_date}'.format(**d)
# #
# # # str2 = '{age},{name}'.format( name = 'tsy',age = 21)
# # # print(str2)
# # attr = ['staff_id', 'name', 'age', 'phone', 'dept', 'enroll_date']
# # value = ['2', 'Alex Li', '22', '13651054608', '"IT"', '2013-04-01']
# # # L = list(zip(attr, value))
# # for i in attr:
# #     d[i] = value[attr.index(i)]
# #
# def file_read(file):
#     with open(file, 'r', encoding='utf8') as f:
#         res = [line.strip().split(',') for line in f]
#         staff_info = [{'staff_id': i[0], 'name': i[1], 'age': i[2], 'phone': i[3], 'dept': i[4],
#                        'enroll_date': i[5]} for i in res]
#         return staff_info
#
# # fuhao = ['>', '=', '<', '>=', '<=', '!=']
# # where = ['dept', '=', '"HR"', 'and', 'age', '>', '22']
#
#
# where = ['age', '>', '22', 'and', 'dept', '=', '"HR"']
# logical = ['and', 'or', 'not']
#
#
# res = file_read('info.txt')
# d = [{'staff_id': '1', 'name': 'Alex Li', 'age': '22', 'phone': '13651054608', 'dept': '"IT"', 'enroll_date': '2013-04-01'},
#      {'staff_id': '2', 'name': 'Jack Wang', 'age': '30', 'phone': '13304320533', 'dept': '"HR"', 'enroll_date': '2015-05-03'},
#      {'staff_id': '3', 'name': 'Rain Liu', 'age': '25', 'phone': '13832352322', 'dept': '"Sales"', 'enroll_date': '2016-04-22'},
#      {'staff_id': '4', 'name': 'Mack Cao', 'age': '40', 'phone': '13531453444', 'dept': '"HR"', 'enroll_date': '2009-03-01'},
#      ]
# print(res)
# s1 = list(set(where) & set(logical))
# if s1:
#     print('符合多个条件才删除')
#     condition1 = where[0:where.index(s1[0])]
#     # print(condition1)
#     if '=' in condition1:
#         condition1[1] = '=='
#     print(condition1)
#     condition2 = where[where.index(s1[0])+1:]
#     if '=' in condition2:
#         condition2[1] = '=='
#     print(condition2)
#
#     # print('---->', )
#
#     # def f(d1):
#     #     eval(d1[condition1[0]]+condition1[1]+condition1[2]) and eval(d1[condition2[0]]+condition2[1]+condition2[2])
#     L = list(filter(lambda x: not(eval(x[condition1[0]] + condition1[1] + condition1[2]) and eval(x[condition2[0]] + condition2[1] + condition2[2])), res))
#     print(L)
#     # print(set(L))
#     str2 = ''
#     for item in L:
#         print(list(item.values()))
#         # for j in (list(item.values())):
#         #     str2 += j
#         str2 += ','.join(item.values())
#         str2 += '\n'
#     print(str2)
# else:
#     print('删除条件只有一个')

def file_alter(file, old_str):
    str1 = ''
    with open(file, 'r') as f:
        for i in f:
            print('iiiiii>>', i)
            if i.startswith(old_str):
                continue
            str1 += i
    print(str1)
    with open(file, 'w') as f1:
        f1.write(str1)

account = input('>>输入你要解结的账号:')
file_alter('info.txt', account)







# for item in where:
#     if item.isalpha():
#         print(item)
#         where.remove(item)
# print(where)
# print()
