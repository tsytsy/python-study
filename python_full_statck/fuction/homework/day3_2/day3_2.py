import time


def isnumber(aString):
    try:
        float(aString)
        return True
    except:
        return False


def info_listdic_to_str(res):
    str1 = ''
    for d in res:
        count = 0
        for line in d.values():
            if count == 4:
                str1 = str1 + line + '\n'
            else:
                str1 = str1 + line + ','
                count += 1
    return str1


def admin_file_alter(file, old_str):
    str1 = ''
    with open(file, 'r') as f:
        for i in f:
            if i.startswith(old_str):
                continue
            str1 += i
    with open(file, 'w') as f1:
        f1.write(str1)


def log_file_read(file):
    with open(file, 'r') as f:
        lines = [line.strip().split(',') for line in f]
        res = [{'account': i[0], 'passwd': i[1]} for i in lines]
        return res


def info_file_read(file):
    with open(file, 'r') as f:
        lines = [line.strip().split(',') for line in f]
        res = [{'account': i[0], 'passwd': i[1], 'balance': i[2], 'arrears': i[3], 'overdraft': i[4]} for i in lines]
        return res


def info_append(file, content):
    with open(file, 'a') as f:
        f.write(content)


def login():
    welcome = '''
1. 管理员登录
2. 用户登录
3. 退出
           '''
    while True:
        print(welcome)
        choice = input('>>输入数字进入相应登录操作:')
        if choice not in ['1', '2', '3']:
            print('输入错误，请重新输入')
        else:
            return choice


def admin_login():
    count = 0
    while count < 3:
        d = {}
        account = input('>>请输入管理员账号：')
        passwd = input('>>请输入你的密码：')
        d['account'] = account
        d['passwd'] = passwd
        res = log_file_read('admin_login.txt')
        if d in res:
            print('login successful')
            admin_func_choice()
            break
        else:
            print('account or passwd wrong')
            count += 1
    else:
        print('你已经尝试了三次登入，请稍后再试一下')


def user_login():
    count = 0
    flag = True
    while flag:
        account = input('>>请输入你的账号：')
        passwd = input('>>请输入你的密码：')
        res_lock = info_file_read('lock_user.txt')
        res = info_file_read('user_info.txt')
        for d in res_lock:
            if d['account'] == account and d['passwd'] == passwd:
                print('Sorry,your account has been locked')
                exit()
        for d in res:
            if d['account'] == account and d['passwd'] == passwd:
                print('login successful')
                user_func_choice(account)
                flag = False
                break
        else:
            print('account or passwd wrong')
            count += 1
            if count == 3:
                print('你已经尝试了三次登入，请稍后再试一下')
                break


def user_func_choice(acoount):
    user_function_liststr = '''
                1. 取款
                2. 存款
                3. 转账
                4. 还款
                5. 打印历史记录
                6. 查看余额
                7. 退出
                '''
    user_function_dict = {
        '1': user_withdrawal,
        '2': user_deposit,
        '3': user_transfer,
        '4': user_repayment,
        '5': user_history_record,
        '6': user_search_balance,
        '7': user_quit2
    }
    while True:
        print(user_function_liststr)
        choice = input('>>输入你需要的服务:')
        if choice not in ['1', '2', '3', '4', '5', '6', '7']:
            print('输入错误，请重新输入')
            continue
        else:
            user_function_dict[choice](acoount)


def user_withdrawal(account):
    '''
    1. 取出金额先余额里减钱，如果余额里没有钱，可以线欠着，如果欠款达到透支额，那么取钱失败
    2. 在用户信息中更新余额，欠款数值
    3. 取钱记录要保存在历史记录中
    '''
    res = info_file_read('user_info.txt')
    index = None
    for d in res:
        if account == d['account']:
            index = res.index(d)
    print(index)
    money = float(input(">>取出金额:"))
    if money <= float(res[index]['balance']):
        new_balance = str(float(res[index]['balance'])-money)
        res[index]['balance'] = new_balance
        str1 = info_listdic_to_str(res)
        print(str1)
        with open('user_info.txt', 'w') as f:
            f.write(str1)
        print('取款完成')
        time1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        record = '{},{},{},{}'.format(time1, account, 'withdraw', money) + '\n'
        info_append('atm_record.txt', record)
    elif money + float(res[index]['arrears']) <= float(res[index]['overdraft']):
        new_arrears = str(float(res[index]['arrears'])+money)
        res[index]['arrears'] = new_arrears
        str1 = info_listdic_to_str(res)
        with open('user_info.txt', 'w') as f:
            f.write(str1)
        print('你的余额不足，从透支额中取款完成')
        time1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        record = '{},{},{},{}'.format(time1, account, 'withdraw', money) + '\n'
        info_append('atm_record.txt', record)
    else:
        print('余额不足')


def user_deposit(account):
    res = info_file_read('user_info.txt')
    print(res)
    index = None
    for d in res:
        if account == d['account']:
            index = res.index(d)
    print(index)
    money = float(input(">>存入金额:"))
    new_balance = str(float(res[index]['balance']) + money)
    res[index]['balance'] = new_balance
    str1 = info_listdic_to_str(res)
    with open('user_info.txt', 'w') as f:
        f.write(str1)
    print('存款完成')
    time1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    record = '{},{},{},{}'.format(time1, account, 'deposit', money) + '\n'
    info_append('atm_record.txt', record)


def user_transfer(account):
    '''
     1. 转账先从余额里减钱，如果余额里没有钱，可以线欠着，如果欠款达到透支额，那么转账失败
     2. 在用户信息中更新余额，欠款数值
     3. 取钱记录要保存在历史记录中
     4. 在用户信息中更新被转账账号数据
     '''
    res = info_file_read('user_info.txt')
    account_list = []
    for d1 in res:
        account_list.append(d1['account'])
    print(account_list)
    print(res)
    index = None
    to_index = None
    for d in res:
        if account == d['account']:
            index = res.index(d)
    print(index)
    while True:
        to_who = input('>>对方账号,退出按q:')
        if to_who == 'q':
            return
        elif to_who not in account_list:
            print('不存在这个账号，重新输入')
            continue
        break

    for d in res:
        if to_who == d['account']:
            to_index = res.index(d)
    print(to_index)
    money = float(input(">>转账金额:"))
    str1 = ''
    if money <= float(res[index]['balance']):
        new_balance = str(float(res[index]['balance']) - money)
        res[index]['balance'] = new_balance
        res[to_index]['balance'] = str(float(res[to_index]['balance']) + money)
        str1 = info_listdic_to_str(res)
        with open('user_info.txt', 'w') as f:
            f.write(str1)
        print('转账完成')
        time1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        record = '{},{},{},{},{}'.format(time1, account, 'transfer to', to_who, money) + '\n'
        info_append('atm_record.txt', record)
    elif money + float(res[index]['arrears']) <= float(res[index]['overdraft']):
        new_arrears = str(float(res[index]['arrears']) + money)
        res[index]['arrears'] = new_arrears
        res[to_index]['balance'] = str(float(res[to_index]['balance']) + money)
        str1 = info_listdic_to_str(res)
        with open('user_info.txt', 'w') as f:
            f.write(str1)
        print('你的余额不足，从透支额转账完成')
        time1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        record = '{},{},{},{},{}'.format(time1, account, 'transfer to', to_who, money) + '\n'
        info_append('atm_record.txt', record)
    else:
        print('余额不足')
    pass


def user_repayment(account):
    '''
    1. 自己本身可以还款任意金额，
    '''
    res = info_file_read('user_info.txt')
    print(res)
    index = None
    for d in res:
        if account == d['account']:
            index = res.index(d)
    print(index)
    while True:
        pay_debt = input('>>请输入还款金额，不还款退出按q:')
        if pay_debt == 'q':
            return
        pay_debt = float(pay_debt)
        if pay_debt > float(res[index]['arrears']):
            print('欠款没有达到这个这个金额，不用还这么多')
            continue
        elif pay_debt > float(res[index]['balance']):
            print('您的余额不足，还款金额超过了您的余额')
            continue
        else:
            break
    res[index]['balance'] = str(float(res[index]['balance']) - pay_debt)
    res[index]['arrears'] = str(float(res[index]['arrears']) - pay_debt)
    str1 = info_listdic_to_str(res)
    with open('user_info.txt', 'w') as f:
        f.write(str1)
    print('还款完成')
    time1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    record = '{},{},{},{}'.format(time1, account, 'pay debt', pay_debt) + '\n'
    info_append('atm_record.txt', record)


def user_history_record(account):
    L = []
    with open('atm_record.txt', 'r') as f:
        for line in f:
            # print(line)
            new_line = line.strip().split(',')
            # print(new_line)
            if account in new_line:
                L.append(line)
    print(L)
    for line in L:
        print(line)



def user_search_balance(account):
    res = info_file_read('user_info.txt')
    for d in res:
        if account == d['account']:
            index = res.index(d)
    print('你的余额为:%s' % res[index]['balance'])
    print('你的欠款为:%s' % res[index]['arrears'])
    print('你的透支额为:%s' % res[index]['overdraft'])

def user_quit2(account):
    exit()

'---------------------------------------------------------------------'


def admin_func_choice():
    function_liststr = '''
            1. 添加账号
            2. 冻结用户
            3. 解冻用户
            4. 查询用户
            5. 退出
            6. 指定用户透支额
            '''
    function_dict = {
        '1': user_add,
        '2': user_freeze,
        '3': user_unfreeze,
        '4': user_search,
        '5': user_quit,
        '6': user_overdraft
    }
    while True:
        print(function_liststr)
        choice = input('>>选择你需要的服务：')
        if choice not in ['1', '2', '3', '4', '5', '6']:
            print('输入错误，请重新输入')
            continue
        else:
            function_dict[choice]()


#添加账号
# def user_add(account, passwd, balance=0, arrears=0, overdraft=0):
def user_add():
    print("你需要填入以下信息")
    account = input('>>账号:')
    passwd = input('>>密码:')
    balance = input('>>余额:')
    arrears = input('>>欠款:')
    overdraft = input('>>透资额:')
    str1 = '{0},{1},{2},{3},{4}'.format(account, passwd, balance, arrears, overdraft) + '\n'
    info_append('user_info.txt', str1)


#冻结用户
def user_freeze():
    res = info_file_read('user_info.txt')
    str2 = ''
    account = input('>>输入你要冻结的账号:')
    for d in res:
        if account in d.values():
            for j in d.values():
                str2 = str2 + j + ','
    str2 += '\n'
    info_append('lock_user.txt', str2)
    print('***************冻结成功***************')


#解冻用户
def user_unfreeze():
    print('被冻结的账户如下')
    res = info_file_read('lock_user.txt')
    for d in res:
        print(d)
    account = input('>>输入你要解结的账号:')
    admin_file_alter('lock_user.txt', account)
    print('解冻成功')


def user_search():
    res = info_file_read('user_info.txt')
    print('********查询结果如下*******')
    for d in res:
        print(d)


def user_quit():
    exit()


def user_overdraft():

    res = info_file_read('user_info.txt')
    account_list = []
    for d1 in res:
        account_list.append(d1['account'])

    while True:
        account = input('>>对方账号,退出按q:')
        if account == 'q':
            return
        elif account not in account_list:
            print('不存在这个账号，重新输入')
            continue
        break

    index = None
    for d in res:
        if account == d['account']:
            index = res.index(d)
    # print(index)
    while True:
        overdraft = input('>>输入用户的透支额，退出请按q:')
        if overdraft == 'q':
            return
        elif not isnumber(overdraft):
            print('not a number')
            continue
        break
    res[index]['overdraft'] = overdraft
    str1 = info_listdic_to_str(res)
    with open('user_info.txt', 'w') as f:
        f.write(str1)


if __name__ == '__main__':

    user_choice = login()
    if user_choice == '1':
        admin_login()
    elif user_choice == '2':
        user_login()
    else:
        exit()
