from core import auth
from core import logger
from core import regist
from conf import settings
from core import db_handler
import os
import json
acc_log = logger.logger('access')
user_data = {
    'account_id': None,
    'is_authenticated': False,
    'account_data': None
}



def search_userinfo():
    pass

def repay():
    pass


def transfer():
    pass


def user_quit():
    pass


def interaction(acc_data):
    menu = '''
    1. 查询用户信息
    2. 取款
    3. 存款
    4. 转账
    5. 退出
    '''
    menu_dic = {
        '1': search_userinfo,
        '2': withdrow,
        '3': repay,
        '4': transfer,
        '5': user_quit
    }
    flag = False
    while not flag:
        print(menu)
        choice = input('choose your service:')
        if choice == 'b':
            flag = True
            continue
        if choice in menu_dic:
            menu_dic[choice](acc_data)
        else:
            print('input your need service')


def withdrow(acc_data):
    # print(acc_data)
    path1 = db_handler.db_handler(settings.DATABASE)
    account_file = os.path.join(path1, 'accounts', acc_data['id'] + '.json')
    transation_log = logger.logger('transaction')
    wmount = input('the amount of withdrow:')
    if wmount.isdigit():
        old_balance = acc_data['balance']
        if int(wmount) < old_balance:
            new_balance = old_balance - int(wmount)
            acc_data['balance'] = new_balance
            with open(account_file, 'w') as f:
                f.write(json.dumps(acc_data))
            transation_log.info('%s withdow %s money' % (acc_data['id'], int(wmount)))
        else:
            print('your balance is not enough')
    else:
        print('invaild number of amount')

def register_or_loggin():
    welcome = '''
        1. 注册
        2. 登录
        '''
    welcome_dic = {
        '1': regist.regist,
        '2': auth.acc_login
    }
    flag = False
    while not flag:
        print(welcome)
        choice = input('>>input your choice:')
        if choice == 'b':
            print('you will exit this system')
            exit()

        elif choice not in welcome_dic:
            print('your choice wrong,please input your choice')
            continue

        elif choice == '1':
            flag = welcome_dic[choice]()
            exit()
        elif choice == '2':
            (flag, acc_data) = welcome_dic[choice](user_data, acc_log)
    return acc_data

def run():
    acc_data = register_or_loggin()
    interaction(acc_data)