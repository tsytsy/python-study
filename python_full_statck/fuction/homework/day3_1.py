def file_read(file):
    with open(file, 'r', encoding='utf8') as f:
        f.seek(0, 0)
        res = [line.strip().split(',') for line in f]
        staff_info = [{'staff_id': i[0], 'name': i[1], 'age': i[2], 'phone': i[3], 'dept': i[4],
                       'enroll_date': i[5]} for i in res]
        return staff_info


def file_append(file, content):
    with open(file, 'a') as f:
        f.write(content+'\n')
        print('add successful')
        f.flush()
        f.close()


#删除和修改都用此函数
def file_alter(file,content):
    with open('info.txt', 'w') as f:
        f.write(content)
        print('alter successful')


def list_to_str(res):
    str1 = ''
    for item in res:
        # print(list(item.values()))
        str1 += ','.join(item.values())
        str1 += '\n'
    return str1

#查询
'''
可进行模糊查询，语法至少支持下面3种:
select name,age from staff_table where age > 22
select  * from staff_table where dept = "IT"
select  * from staff_table where enroll_date like 2013
'''


def select(user_input):
    staff_info = file_read('info.txt')
    user_input = user_input.split()
    # 过滤,采用filter过滤，过滤条件为where
    where = user_input[user_input.index('where')+1:]
    if '=' in where:
        where[1] = '=='
    if 'like' in where:
        L = list(filter(lambda x: where[-1] in x[where[0]], staff_info))
    else:
        L = list(filter(lambda x: eval(x[where[0]]+where[1]+where[2]), staff_info))
    #显示内容
    sele_contact = user_input[1].split(',')
    def map_fuc(dic):
        return tuple([dic[i] for i in sele_contact])
    if '*' in sele_contact:
        L1 = L
    else:
        L1 = list(map(map_fuc, L))
    print('查到符合条件的数据有{}条,如下所示'.format(len(L1)))
    for item in L1:
        print(item)

#可创建新员工纪录，以phone做唯一键，staff_id需自增
'''
insert staff_table (column1,column2,column3,...) values (value1,value2,value3,...);
insert info.txt name,age,phone,dept,enroll_date values tsy,22,13651054608,"IT",2017-04-01 
1. phone做唯一key,不能重复
2, staff_id自增
3. 信息可能输入不完整
'''


def insert(user_input):
    phone_list = []
    res = file_read('info.txt')
    for dic in res:
        phone_list.append(dic['phone'])
    user_input = user_input.split()
    file = user_input[1]
    count = int(res[-1]['staff_id'])+1
    attr = user_input[2].split(',')
    value = user_input[-1].split(',')
    d = {
        'name': ' ',
        'age': ' ',
        'phone': ' ',
        'dept': ' ',
        'enroll_date': ' '
    }
    for i in attr:
        d[i] = value[attr.index(i)]
    if d['phone'] in phone_list:
        print('phone exist, please try it again')
    else:
        str1 = "{staff_id},{name},{age},{phone},{dept},{enroll_date}".format(staff_id=str(count), **d)
        file_append(file, str1)


#可删除指定员工信息纪录，输入员工id，即可删除
'''
delete from info.txt where dept = "HR" and age > 22
delete from info.txt where age > 22 and dept = "HR"
delete from info.txt where dept = "IT"
delete from info.txt where staff_id = 5
找到staff_id，删除信息
支持多个条件删除以及范围删除
'''


def delete(user_input):
    user_input = user_input.split()
    where = user_input[user_input.index('where')+1:]
    file = user_input[2]
    res = file_read('info.txt')
    logical = ['and', 'or', 'not']
    s1 = list(set(where) & set(logical))
    if s1:
        print('符合多个条件才删除')
        condition1 = where[0:where.index(s1[0])]
        if '=' in condition1:
            condition1[1] = '=='
        condition2 = where[where.index(s1[0]) + 1:]
        if '=' in condition2:
            condition2[1] = '=='
        L = list(filter(lambda x: not (eval(x[condition1[0]] + condition1[1] + condition1[2]) and
                                       eval(x[condition2[0]] + condition2[1] + condition2[2])), res))
        file_alter(file, list_to_str(L))
    else:
        print('删除条件只有一个')
        if '=' in where:
            where[1] = '=='
        L = list(filter(lambda x: not(eval(x[where[0]] + where[1] + where[2])), res))
        file_alter(file, list_to_str(L))


# 可以使用UPDATE命令修改指定员工信息
'''
update info.txt set dept = "Market" where dept = "IT"
update info.txt set dept = "IT" where dept = "Market"
'''

def update(user_input):
    res = file_read('info.txt')
    user_input = user_input.split()
    file = user_input[1]
    change = user_input[user_input.index('set')+1:user_input.index('where')]
    where = user_input[user_input.index('where')+1:]
    if '=' in where:
        where[1] = '=='
    for item in res:
        if eval(item[where[0]]+where[1]+where[2]):
            item[change[0]] = change[2]
    file_alter(file, list_to_str(res))


cmd = {
    'select': select,
    'delete': delete,
    'insert': insert,
    'update': update
}
while True:
    print("对数据库进行增删改查操作，请输入命令，输入q退出程序")
    user_input = input(">>").strip()
    if user_input == 'q':
        break
    key = user_input.split()[0]
    if key in cmd:
        cmd[key](user_input)
    else:
        print("请输入数据库命令")