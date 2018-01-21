with open('info.txt', 'r', encoding='utf8') as f:
    res = [line.strip().split(',') for line in f]
    staff_info = [{'staff_id': i[0], 'name': i[1], 'age': int(i[2]), 'phone': i[3], 'dept': i[4],
                   'enroll_date': i[5]} for i in res]


d = [{'dept': 'IT', 'name': 'tsy'},{'dept': 'HR', 'name': 'tty'}]

where = ['dept', '=', 'HR']


def func(d1):
    tiaojian = [d1[where[0]], where[1],where[2]]
    print(tiaojian)
    condition = eval(''.join(tiaojian))
    print(condition)
func(d)

#
# f1 = filter(lambda x: eval(x[where[0]] + '==' + where[2]), staff_info)
# print(f1)
# for i in f1:
#     print('----',i)