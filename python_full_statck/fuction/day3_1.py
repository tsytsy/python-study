#查询
'''
可进行模糊查询，语法至少支持下面3种:
　　select name,age from staff_table where age > 22
　　select  * from staff_table where dept = "IT"
   select  * from staff_table where enroll_date like "2013"
查到的信息，打印后，最后面还要显示查到的条数
'''

with open('info.txt', 'r', encoding='utf8') as f:
    res = [line.strip().split(',') for line in f]
    staff_info = [{'staff_id': i[0], 'name': i[1], 'age': i[2], 'phone': i[3], 'dept': i[4],
                   'enroll_date': i[5]} for i in res]



#模拟数据库的操作
'''
select name,age from staff_table where age > 22
select  * from staff_table where dept = "IT"
select  * from staff_table where enroll_date like "2013"
'''


def select(user_input):
    print(user_input)
    user_info = user_input.split()
    where = user_info[user_info.index('where')+1:]  #过滤条件  age > 22

    print(where)
    if '=' in where:
        where[1] = '=='

    L = list(filter(lambda x: eval(x[where[0]]+where[1]+where[2]), staff_info))
    print(L)

    # if 'like' in where:
    #     L = list(filter(lambda x: where[-1] in where[0], staff_info))
    # elif '=' in where:
    #     L = list(filter(lambda x: eval((x[where[0]])+where[1]+where[2]), staff_info))
    #     # L = list(filter(lambda x: eval(''.join([x[where[0]], '==', where[2]])), staff_info))
    # else:
    #     L = list(filter(lambda x: eval((x[where[0]])+where[1]+where[2]), staff_info))
    # print(L)





    print('from select')


def delete(user_input):
    print('from delect')


def update(user_input):
    print('from update')


def add(user_input):
    print('from add')


cmd = {
    'select': select,
    'delete': delete,
    'add': add,
    'update': update
}
while True:
    user_input = input(">>").strip()
    key = user_input.split()[0]

    if key in cmd:
        cmd[key](user_input)
    else:
        print("input your wantta cmd")




