import json
import os
from conf import settings
from core import db_handler

def regist():
    reg_dic = {
        'id': None,
        'password': None,
        'credit': 15000,
        'balance': 15000,
        'enroll_date': '2016-01-02',
        'expire_date': '2021-01-01',
        'pay_day': 22,
        'status': 0  # 0 = normal, 1 = locked, 2 = disabled
    }

    account_id = input('id:')
    path1 = db_handler.db_handler(settings.DATABASE)
    account_file = os.path.join(path1, 'accounts', account_id + '.json')
    if os.path.exists(account_file):
        print('account has been registed')
        return
    account_passwd = input('passwd (a six int num):')
    reg_dic['id'] = account_id
    reg_dic['password'] =account_passwd
    reginfo_to_file(reg_dic)
    print('register succssful')
    return True


def reginfo_to_file(account_data):
    print(account_data)
    path1 = db_handler.db_handler(settings.DATABASE)
    print(path1)
    file_path = os.path.join(path1, 'accounts', account_data['id'])
    print(file_path)
    with open(file_path, 'w') as f:
        f.write(json.dumps(account_data))
    # json.dump(account_data, open(file_path))
    os.rename(file_path, '.'.join([file_path, 'json']))



